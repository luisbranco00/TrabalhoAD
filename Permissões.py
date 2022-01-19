def run():
    from django.contrib.auth.models import User, Group, Permission
    mygroup, created = Group.objects.get_or_create(name='Administrador')
    permissao1 = Permission.objects.get(name='Adiciona_Utilizador')
    permissao2 = Permission.objects.get(name='Ver_Utilizadores')
    permissao3 = Permission.objects.get(name='Adicionar_Utente')
    permissao4 = Permission.objects.get(name='Remover_Utente')
    permissao5 = Permission.objects.get(name='Ver_Utente')
    permissao6 = Permission.objects.get(name='Adicionar_Médico')
    permissao7 = Permission.objects.get(name='Adicionar_Farmaceutico')
    permissao8 = Permission.objects.get(name='Remover_Utilizador')
    permissao9 = Permission.objects.get(name='Remover_Medico')
    permissao10 = Permission.objects.get(name='Remover_Farmaceutico')
    permissao11 = Permission.objects.get(name='Ver_Medico')
    permissao12 = Permission.objects.get(name='Ver_Farmaceutico')
    mygroup.permissions.add(permissao1, permissao2, permissao3, permissao4, permissao5, permissao6, permissao7,
                            permissao8, permissao9, permissao10, permissao11, permissao12)
    mygroup.save()

    mygroup, created = Group.objects.get_or_create(name='Medico')
    permissao1 = Permission.objects.get(name='Ver_Utentes')
    permissao2 = Permission.objects.get(name='Marca_consultas')

    permissao3 = Permission.objects.get(name='Elimina_Consultas')
    permissao4 = Permission.objects.get(name='Ver_Medicos')

    permissao5 = Permission.objects.get(name='Ver_Consultas')

    mygroup.permissions.add(permissao1, permissao2, permissao3, permissao4, permissao5)
    mygroup.save()

    mygroup, created = Group.objects.get_or_create(name='Farmaceutico')
    permissao1 = Permission.objects.get(name='Compra_Medicamentos')
    permissao2 = Permission.objects.get(name='Prescreve_medicamento')
    permissao3 = Permission.objects.get(name='Ver_Medicamentos')
    permission4 = Permission.objects.get(name='Adiciona_Medicamentos')
    permissao5 = Permission.objects.get(name='Ver_Prescrições')

    mygroup.permissions.add(permissao1, permissao2, permissao3, permission4, permissao5)
    mygroup.save()
