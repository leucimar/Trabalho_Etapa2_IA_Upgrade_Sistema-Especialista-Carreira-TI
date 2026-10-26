"""Encadeamento para frente com evidências produzidas pelo Experta."""
from dataclasses import dataclass
import collections
import collections.abc

# frozendict 1.2, dependência fixada do Experta, usa o alias removido no Python 3.10.
# Compatibilidade isolada, aplicada antes do primeiro import do motor.
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
from experta import Fact, KnowledgeEngine, Rule
from .catalogo import TRILHAS, OPCOES


class Perfil(Fact):
    """Respostas validadas da entrevista."""


class Evidencia(Fact):
    """Conclusão de uma regra: trilha, identificador, pontos e motivo."""


class Consultor(KnowledgeEngine):
    """Trinta regras cruzadas independentes; nenhuma seleciona por ordem de disparo."""

    @Rule(Perfil(atividade="logica", entrega="apis"))
    def r01(self):
        self.declare(Evidencia(trilha="backend", regra="R01", pontos=6, motivo='Atividade e entrega convergem para Desenvolvimento Back-end.'))

    @Rule(Perfil(atividade="logica", ferramenta="python"))
    def r02(self):
        self.declare(Evidencia(trilha="backend", regra="R02", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Desenvolvimento Back-end.'))

    @Rule(Perfil(entrega="apis", objetivo="tecnico"))
    def r03(self):
        self.declare(Evidencia(trilha="backend", regra="R03", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam Desenvolvimento Back-end.'))

    @Rule(Perfil(atividade="visual", entrega="interfaces"))
    def r04(self):
        self.declare(Evidencia(trilha="frontend", regra="R04", pontos=6, motivo='Atividade e entrega convergem para Desenvolvimento Front-end & UI/UX.'))

    @Rule(Perfil(atividade="visual", ferramenta="javascript"))
    def r05(self):
        self.declare(Evidencia(trilha="frontend", regra="R05", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Desenvolvimento Front-end & UI/UX.'))

    @Rule(Perfil(entrega="interfaces", objetivo="tecnico"))
    def r06(self):
        self.declare(Evidencia(trilha="frontend", regra="R06", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam Desenvolvimento Front-end & UI/UX.'))

    @Rule(Perfil(atividade="modelos", entrega="previsoes"))
    def r07(self):
        self.declare(Evidencia(trilha="ciencia", regra="R07", pontos=6, motivo='Atividade e entrega convergem para Ciência de Dados e Machine Learning.'))

    @Rule(Perfil(atividade="modelos", ferramenta="python"))
    def r08(self):
        self.declare(Evidencia(trilha="ciencia", regra="R08", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Ciência de Dados e Machine Learning.'))

    @Rule(Perfil(entrega="previsoes", matematica="alta"))
    def r09(self):
        self.declare(Evidencia(trilha="ciencia", regra="R09", pontos=2, motivo='Entrega e afinidade estatística alta reforçam Ciência de Dados e Machine Learning.'))

    @Rule(Perfil(atividade="pipelines", entrega="dados"))
    def r10(self):
        self.declare(Evidencia(trilha="engenharia", regra="R10", pontos=6, motivo='Atividade e entrega convergem para Engenharia de Dados.'))

    @Rule(Perfil(atividade="pipelines", ferramenta="sql"))
    def r11(self):
        self.declare(Evidencia(trilha="engenharia", regra="R11", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Engenharia de Dados.'))

    @Rule(Perfil(entrega="dados", objetivo="tecnico"))
    def r12(self):
        self.declare(Evidencia(trilha="engenharia", regra="R12", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam Engenharia de Dados.'))

    @Rule(Perfil(atividade="seguranca", entrega="protecao"))
    def r13(self):
        self.declare(Evidencia(trilha="seguranca", regra="R13", pontos=6, motivo='Atividade e entrega convergem para Cibersegurança (Security / Pentesting).'))

    @Rule(Perfil(atividade="seguranca", ferramenta="linux"))
    def r14(self):
        self.declare(Evidencia(trilha="seguranca", regra="R14", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Cibersegurança (Security / Pentesting).'))

    @Rule(Perfil(entrega="protecao", objetivo="tecnico"))
    def r15(self):
        self.declare(Evidencia(trilha="seguranca", regra="R15", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam Cibersegurança (Security / Pentesting).'))

    @Rule(Perfil(atividade="automacao", entrega="confiabilidade"))
    def r16(self):
        self.declare(Evidencia(trilha="devops", regra="R16", pontos=6, motivo='Atividade e entrega convergem para DevOps & SRE.'))

    @Rule(Perfil(atividade="automacao", ferramenta="linux"))
    def r17(self):
        self.declare(Evidencia(trilha="devops", regra="R17", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam DevOps & SRE.'))

    @Rule(Perfil(entrega="confiabilidade", objetivo="tecnico"))
    def r18(self):
        self.declare(Evidencia(trilha="devops", regra="R18", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam DevOps & SRE.'))

    @Rule(Perfil(atividade="arquitetura", entrega="infraestrutura"))
    def r19(self):
        self.declare(Evidencia(trilha="cloud", regra="R19", pontos=6, motivo='Atividade e entrega convergem para Computação em Nuvem (Cloud Architecture).'))

    @Rule(Perfil(atividade="arquitetura", ferramenta="cloud"))
    def r20(self):
        self.declare(Evidencia(trilha="cloud", regra="R20", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Computação em Nuvem (Cloud Architecture).'))

    @Rule(Perfil(entrega="infraestrutura", objetivo="tecnico"))
    def r21(self):
        self.declare(Evidencia(trilha="cloud", regra="R21", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam Computação em Nuvem (Cloud Architecture).'))

    @Rule(Perfil(atividade="mobile", entrega="aplicativos"))
    def r22(self):
        self.declare(Evidencia(trilha="mobile", regra="R22", pontos=6, motivo='Atividade e entrega convergem para Desenvolvimento Mobile.'))

    @Rule(Perfil(atividade="mobile", ferramenta="mobile"))
    def r23(self):
        self.declare(Evidencia(trilha="mobile", regra="R23", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Desenvolvimento Mobile.'))

    @Rule(Perfil(entrega="aplicativos", objetivo="tecnico"))
    def r24(self):
        self.declare(Evidencia(trilha="mobile", regra="R24", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam Desenvolvimento Mobile.'))

    @Rule(Perfil(atividade="testes", entrega="qualidade"))
    def r25(self):
        self.declare(Evidencia(trilha="qa", regra="R25", pontos=6, motivo='Atividade e entrega convergem para Engenharia de Qualidade e Testes (QA).'))

    @Rule(Perfil(atividade="testes", ferramenta="testes"))
    def r26(self):
        self.declare(Evidencia(trilha="qa", regra="R26", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Engenharia de Qualidade e Testes (QA).'))

    @Rule(Perfil(entrega="qualidade", objetivo="tecnico"))
    def r27(self):
        self.declare(Evidencia(trilha="qa", regra="R27", pontos=2, motivo='Entrega e objetivo de aprofundamento técnico reforçam Engenharia de Qualidade e Testes (QA).'))

    @Rule(Perfil(atividade="negocio", entrega="valor"))
    def r28(self):
        self.declare(Evidencia(trilha="produto", regra="R28", pontos=6, motivo='Atividade e entrega convergem para Gestão de Produtos (Product Management).'))

    @Rule(Perfil(atividade="negocio", ferramenta="gestao"))
    def r29(self):
        self.declare(Evidencia(trilha="produto", regra="R29", pontos=3, motivo='Atividade diária e ferramenta declarada reforçam Gestão de Produtos (Product Management).'))

    @Rule(Perfil(entrega="valor", objetivo="pessoas"))
    def r30(self):
        self.declare(Evidencia(trilha="produto", regra="R30", pontos=2, motivo='Entrega e objetivo de trabalhar com pessoas reforçam Gestão de Produtos (Product Management).'))


@dataclass(frozen=True)
class Resultado:
    recomendacao: str | None
    ranking: list[dict]
    evidencias: list[dict]
    empatadas: list[str]


def recomendar(respostas: dict) -> Resultado:
    """Instância nova por consulta para impedir vazamento entre usuários."""
    if set(respostas) != set(OPCOES):
        raise ValueError('Informe exatamente as cinco dimensões da entrevista.')
    for campo, valor in respostas.items():
        if valor not in OPCOES[campo]:
            raise ValueError(f'Resposta inválida para {campo}: {valor!r}')
    motor = Consultor()
    motor.reset()
    motor.declare(Perfil(**respostas))
    motor.run()
    evidencias = sorted(
        [dict(f) for f in motor.facts.values() if isinstance(f, Evidencia)],
        key=lambda e: e['regra'])
    # Remove metadados internos do Experta da representação pública.
    evidencias = [{k: e[k] for k in ('trilha', 'regra', 'pontos', 'motivo')}
                  for e in evidencias]
    pontos = {t: 0 for t in TRILHAS}
    for e in evidencias:
        pontos[e['trilha']] += e['pontos']
    ordem = sorted(TRILHAS, key=lambda t: (
        -pontos[t],
        -(TRILHAS[t]['atividade'] == respostas['atividade']),
        -(TRILHAS[t]['entrega'] == respostas['entrega']), t))
    ranking = [dict(trilha=t, pontos=pontos[t]) for t in ordem]
    melhor = pontos[ordem[0]]
    empatadas = [t for t in ordem if pontos[t] == melhor] if melhor else []
    return Resultado(ordem[0] if melhor else None, ranking, evidencias, empatadas)
