# Flashcards - IAM, Identity Center e Cross-Account

1. **Quando preferir IAM Identity Center a IAM users?**
   Quando pessoas precisam acessar muitas contas com lifecycle, MFA e grupos controlados por IdP corporativo.

2. **Quando uma IAM role e melhor que um IAM user?**
   Quando o acesso pode ser temporario, assumido por workload, pessoa federada ou outra conta, reduzindo credenciais longas.

3. **Qual sinal aponta para STS AssumeRole?**
   Acesso temporario entre principals e contas, com auditoria de sessao e escopo limitado.

4. **Quando usar resource-based policy em vez de apenas identity policy?**
   Quando o recurso precisa autorizar principals externos diretamente, como em S3, KMS, SQS ou Lambda.

5. **Por que permission set nao e a mesma coisa que role manual?**
   Permission set e modelo do Identity Center para provisionar permissoes em contas; a role e o artefato assumido na conta.

6. **Quando permissions boundary e mais adequado que SCP?**
   Quando o limite deve aplicar a roles/users especificos criados por equipes, nao a conta inteira.

7. **Quando SCP e mais adequado que permissions boundary?**
   Quando a organizacao precisa impedir acoes em uma conta ou OU inteira, inclusive contra administradores locais.

8. **Por que trust policy e diferente de permission policy?**
   Trust policy controla quem pode assumir a role; permission policy controla o que a role pode fazer apos assumida.

9. **Qual risco de usuarios IAM duplicados entre contas?**
   Lifecycle inconsistente, credenciais longas, auditoria fraca e maior chance de acesso residual.

10. **Quando manter acesso break-glass?**
    Para emergencia controlada, com MFA forte, credenciais protegidas, monitoramento, aprovacao e revisao periodica.
