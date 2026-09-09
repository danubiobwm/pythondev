import random
from django.core.management.base import BaseCommand
from faker import Faker
from eventin.models import Evento, Participante, Inscricao
from validate_docbr import CPF


class Command(BaseCommand):
    help = "Popula o banco de dados com informações de eventos e participantes"

    def handle(self, *args, **kwargs):
        fake = Faker("pt_BR")
        cpf_generator = CPF()

        eventos_titulos = [
            "Conferência de Desenvolvimento Web",
            "DevOps Summit 2024",
            "Hackathon de Inovação Tech",
            "JavaScript Experience",
            "Python Brasil Conference",
            "Mobile App Development Forum",
            "Cloud Computing World Expo",
            "Cybersecurity & Data Privacy Summit",
            "Machine Learning & AI Conference",
            "Blockchain & Fintech Symposium",
        ]

        eventos = []
        for titulo in eventos_titulos:
            evento = Evento(
                titulo=titulo,
                descricao=fake.text(max_nb_chars=200),
                local=fake.city(),
                data_evento=fake.date_between(start_date="today", end_date="+30d"),
                horario=fake.time_object(),
                capacidade=random.randint(50, 200),
            )
            eventos.append(evento)

        Evento.objects.bulk_create(eventos)
        self.stdout.write(self.style.SUCCESS(f"{len(eventos)} eventos criados."))

        participantes = []
        emails_usados = set()
        cpfs_usados = set()

        for _ in range(20):
            email = fake.unique.email()
            cpf = cpf_generator.generate()
            while email in emails_usados:
                email = fake.unique.email()
            while cpf in cpfs_usados:
                cpf = cpf_generator.generate()
            emails_usados.add(email)
            cpfs_usados.add(cpf)

            participantes.append(
                Participante(
                    nome=fake.name(),
                    cpf=cpf,
                    email=email,
                    telefone=fake.numerify("## #####-####"),
                )
            )

        Participante.objects.bulk_create(participantes)
        self.stdout.write(self.style.SUCCESS(f"{len(participantes)} participantes criados."))

        eventos_salvos = list(Evento.objects.all())
        participantes_salvos = list(Participante.objects.all())
        inscricoes = []

        for participante in participantes_salvos:
            evento = random.choice(eventos_salvos)
            inscricoes.append(
                Inscricao(evento=evento, participante=participante)
            )

        Inscricao.objects.bulk_create(inscricoes)
        self.stdout.write(self.style.SUCCESS(f"{len(inscricoes)} inscrições criadas."))