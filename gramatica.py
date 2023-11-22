import random

sujeitoSM = ['luiz', 'gabriel', 'daniel', 'matheus', 'pedro',
                                'joao', 'arthur', 'ele', 'voce']
sujeitoSF = ['maria', 'eduarda', 'sabrina', 'juliana', 'janina',
                                'juscelino', 'bruna', 'ela', 'voce']
sujeitoPM = ['voces', 'eles']

# random.choice foi utilizado para simplificar a criacao da gramatica
# ex: eu deveria criar um V: verbo e um V: VA, mas crio um V: podendo escolher entre verbo ou VA
class Gramatica():
        def __init__(self): 
                self.gramatica = {
                'O': random.choice([['sujeitoS', 'V', 'P', 'ACT'], 
                        ['sujeitoP', 'V', 'm', 'P', 'ACT'], 
                        ['sujeitoSM', 'é', 'adjetivo', 'o', 'ACT'], 
                        ['sujeitoSF', 'é', 'adjetivo', 'a', 'ACT'], 
                        ['elas', 'são', 'adjetivo', 'as', 'ACT'],
                        ['sujeitoPM', 'são', 'adjetivo', 'os', 'ACT']]),
                'V': [random.choice(['verbo', 'VA'])],          
                'VA': ['adverbio', 'verbo'],
                'P': [random.choice(['PS', 'PC'])],
                'PS': ['com', random.choice(['sujeitoS', 'substantivo'])],
                'PC': [random.choice(['CP', 'CC'])],
                'CC': ['conjuncao', 'V'],
                'CP': ['para', 'verboInf'],
                'ACT': [random.choice(['.', 'CTN'])],
                'CTN': [',', 'O'],

                'conjuncao': ['e', 'ou', 'logo'],
                'sujeitoS' : sujeitoSM + sujeitoSF,
                'sujeitoP' : sujeitoPM + ['elas'],
                'sujeitoSM' : sujeitoSM,
                'sujeitoSF' : sujeitoSF,
                'sujeitoPM': sujeitoPM,
                'verbo' : ['mata', 'come', 'divide', 'canta',
                        'estuda', 'viaja', 'vive', 'pensa',
                        'parte', 'corrige', 'entrega', 'enche',
                        'frita', 'morre'],
                'verboInf' : ['matar', 'comer', 'dividir', 'cantar',
                        'estudar', 'viajar', 'viver', 'pensar',
                        'partir', 'corrigir', 'entregar', 'encher',
                        'fritar', 'morrer'],
                'adverbio': ['certamente', 'sempre', 'nunca', 'absolutamente'],
                'substantivo': ['pessoa', 'gente', 'mesa', 
                        'casa', 'carro', 'roupa', 'menina', 
                        'menino', 'animal', 'alegria', 'tristeza',
                        'chuva', 'folha', 'cachorro', 'gato'],
                'adjetivo': ['lind', 'rapid', 'burr',
                        'baix', 'ric', 'brasileir', 'fei',
                        'baian', 'alt', 'espert', 'gord', 'magr',
                        'brav', 'rapid', 'calm'],
                }

