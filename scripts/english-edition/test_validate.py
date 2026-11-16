"""Regression and mutation tests for meaningful documentation failures."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import validate as v

SOURCE = '''## Questao 1
Escolha duas alternativas.
A. Primeira alternativa.
B. Segunda alternativa.
C. Terceira alternativa.
**Resposta:** A, C
**Explicacao:** Justificativa original.
'''
TARGET = '''## Question 1
Choose two alternatives.
A. First option.
B. Second option.
C. Third option.
**Answer:** A, C
**Explanation:** Both options meet the explicit constraints.
'''


class ExerciseTests(unittest.TestCase):
    def test_multiple_correct_answers_preserved(self) -> None:
        self.assertEqual(v.exercise_failures(SOURCE, TARGET, {}), [])

    def test_wrong_answer_rejected(self) -> None:
        self.assertTrue(v.exercise_failures(SOURCE, TARGET.replace('A, C', 'B'), {}))

    def test_missing_alternative_rejected(self) -> None:
        self.assertTrue(v.exercise_failures(SOURCE, TARGET.replace('C. Third option.\n', ''), {}))

    def test_missing_question_rejected(self) -> None:
        self.assertTrue(v.exercise_failures(SOURCE, '', {}))

    def test_missing_explanation_rejected(self) -> None:
        self.assertTrue(v.exercise_failures(SOURCE, TARGET.split('**Explanation:**')[0], {}))

    def test_multiselect_requirement_cannot_disappear(self) -> None:
        self.assertTrue(v.exercise_failures(SOURCE, TARGET.replace('Choose two', 'Choose'), {}))

    def test_open_answer_correction_cannot_regress(self) -> None:
        source = '1. Context. **Resposta:** GuardDuty.'
        target = '1. Context. **Answer:** GuardDuty.'
        self.assertTrue(v.exercise_failures(source, target, {1: 'AWS Config.'}))

    def test_flashcard_loss_rejected(self) -> None:
        self.assertTrue(v.structure_failures('1. First\n2. Second\n', '1. First\n', True))


class MarkdownTests(unittest.TestCase):
    def test_unclosed_fence_rejected(self) -> None:
        self.assertIn('unclosed code fence', v.markdown_failures('```python\nx = 1\n'))

    def test_closed_fence_accepted(self) -> None:
        self.assertEqual(v.markdown_failures('```python\nx = 1\n```\n'), [])

    def test_extra_table_cell_rejected(self) -> None:
        self.assertTrue(v.table_failures('| A | B |\n|---|---|\n| a | b | c |'))

    def test_expandable_answer_requires_summary(self) -> None:
        self.assertTrue(v.markdown_failures('<details>Answer</details>'))

    def test_unbalanced_details_rejected(self) -> None:
        self.assertTrue(v.markdown_failures('<details><summary>Answer</summary>'))

    def test_duplicate_and_setext_anchors(self) -> None:
        self.assertEqual(v.anchors('# Repeat\n# Repeat\nSetext\n---\n'), {'repeat', 'repeat-1', 'setext'})

    def test_code_comment_does_not_create_anchor(self) -> None:
        self.assertNotIn('fake', v.anchors('```sh\n# Fake\n```'))

    def test_portuguese_paragraph_rejected(self) -> None:
        self.assertTrue(v.language_failures('Uma empresa precisa de seguranca e governanca.'))

    def test_portuguese_url_is_allowed(self) -> None:
        self.assertEqual(v.language_failures('[Course](https://example.com/migracao/questoes)'), [])

    def test_html_images_and_markdown_anchors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / 'README.md'
            page.write_text('# Topic\n[valid](#topic)\n<img src="missing.png">', encoding='utf-8')
            self.assertEqual(len(v.link_failures(page, root)), 1)
            page.write_text('# Topic\n[bad](#absent)', encoding='utf-8')
            self.assertIn('missing anchor', v.link_failures(page, root)[0])


if __name__ == '__main__':
    unittest.main()
