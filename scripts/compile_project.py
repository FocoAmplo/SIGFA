import compileall

ok = compileall.compile_dir("backend/app", force=True, quiet=1)

print()

if ok:
    print("Projeto compilado com sucesso.")
else:
    print("Existem arquivos com erro.")