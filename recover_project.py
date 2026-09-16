#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Recuperação do Projeto Dicionário Científico
Este script recria toda a estrutura de arquivos testada e aprovada.
"""

import os
import shutil

# Configuração da Raiz
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) if os.path.dirname(os.path.abspath(__file__)) else os.getcwd()

# Estrutura de Diretórios
dirs = [
    "input/taxonomy",
    "data/pt-BR",
    "data/en-US",
    "src",
    "templates",
    "templates/META-INF",
    "output"
]

for d in dirs:
    os.makedirs(os.path.join(ROOT_DIR, d), exist_ok=True)
    print(f"Criada pasta: {d}")

# ==========================================
# 1. TERMOS DE BIOLOGIA (DeCS/MeSH)
# ==========================================

decs_terms = """anatomia
fisiologia
patologia
farmacologia
epidemiologia
etiologia
diagnóstico
terapêutica
profilaxia
imunologia
microbiologia
virologia
parasitologia
genética
oncologia
cardiologia
neurologia
psiquiatria
pediatria
geriatria
obstetrícia
ginecologia
oftalmologia
dermatologia
ortopedia
urologia
nefrologia
gastroenterologia
endocrinologia
hematologia
reumatologia
pneumologia
infectologia
saúde pública
saneamento
toxicologia
radiologia
bioquímica
biofísica
bioestatística
bioética
biossegurança
biotecnologia
genômica
proteômica
metabolômica
transcriptômica
microbioma
resistoma
zoonose
vetor
hospedeiro
patógeno
antígeno
anticorpo
vacina
soro
antibiótico
antiviral
antifúngico
quimioterápico
placebo
ensaio clínico
randomizado
duplo-cego
coorte
caso-controle
transversal
metanálise
revisão sistemática
odds ratio
risco relativo
incidência
prevalência
morbidade
mortalidade
letalidade
sobrevivência
prognóstico
fisiopatologia
semiologia
anamnese
exame físico
hipótese diagnóstica
conduta terapêutica
evolução
alta
óbito
necropsia
histopatologia
citopatologia
imuno-histoquímica
biologia molecular
pcr
sequenciamento
crispr
clonagem
transgênico
knockout
transcrição
tradução
replicação
mutação
polimorfismo
epigenética
apoptose
necrose
autofagia
sinalização celular
receptor
ligante
enzima
substrato
inibidor
agonista
antagonista
farmacocinética
farmacodinâmica
biodisponibilidade
meia-vida
clearance
distribuição
metabolismo
excreção
toxicidade
efeito adverso
interação medicamentosa
contraindicação
precaução
posologia
via de administração
forma farmacêutica
princípio ativo
excipiente
veículo
estabilizante
conservante
cisticercose
esquistossomose
neurocisticercose
taenia solium
schistosoma mansoni
leishmania braziliensis
plasmodium falciparum
ascarís lumbricoides
enterobius vermicularis
strongyloides stercoralis
ancilostomíase
filariose
leptospirose
hanseníase
tuberculose
malária
dengue
zika
chikungunya
febre amarela
raiva
tétano
botulismo
gangrena
sepse
choque séptico
insuficiência renal
insuficiência hepática
insuficiência cardíaca
infarto agudo do miocárdio
acidente vascular cerebral
trombose
embolia
varizes
hemorroida
úlcera péptica
gastrite
hepatite
cirrose
coledocolitíase
pancreatite
apendicite
diverticulite
hérnia
obstrução intestinal
doença inflamatória intestinal
doença de crohn
retocolite ulcerativa
síndrome do intestino irritável
constipação
diarreia
dispepsia
náusea
vômito
hematêmese
melena
icterícia
ascite
esplenomegalia
hepatomegalia
colelitíase
nefrolitíase
cálculo renal
infecção urinária
pielonefrite
glomerulonefrite
síndrome nefrótica
síndrome nefrítica
proteinúria
hematúria
leucocitúria
bacteriúria
uretrite
cistite
prostatite
orquite
epididimite
hidrocele
varicocele
fimose
parafimose
criptorquidia
hipospádia
epispádia
câncer de próstata
câncer de bexiga
câncer de rim
câncer de testículo
câncer de pênis
infertilidade masculina
disfunção erétil
ejaculação precoce
menopausa
andropausa
osteoporose
artrite
artrose
lúpus
fibromialgia
síndrome de sjogren
esclerodermia
polimiosite
dermatomiosite
vasculite
gota
pseudogota
condrocalcinose
bursite
tendinite
tenossinovite
síndrome do túnel do carpo
epicondilite
ombro congelado
cifose
escoliose
lordose
espondilite
espondilose
hérnia de disco
ciatalgia
lombalgia
cervicalgia
dor torácica
fratura
luxação
entorse
distensão
contusão
ferimento
queimadura
congelação
picada de inseto
picada de animal peçonhento
envenenamento
intoxicação
overdose
alergia
anafilaxia
urticária
angioedema
eczema
dermatite
psoríase
acne
rosácea
vitiligo
melasma
alopecia
hirsutismo
onicomicose
tinha
impetigo
celulite infecciosa
abscesso
furúnculo
carbúnculo
erisipela
fasciíte necrosante
miosite
rabdomiólise
síndrome compartimental
úlcera de pressão
úlcera venosa
úlcera arterial
úlcera diabética
pé diabético
gangrena diabética
retinopatia diabética
neuropatia diabética
nefropatia diabética
diabetes tipo 1
diabetes tipo 2
diabetes gestacional
pré-diabetes
hipoglicemia
hiperglicemia
cetoacidose diabética
estado hiperosmolar
obesidade
sobrepeso
desnutrição
caquexia
anorexia
bulimia
transtorno alimentar
deficiência de vitamina
deficiência de mineral
anemia
anemia ferropriva
anemia megaloblástica
anemia falciforme
talassemia
hemofilia
doença de von willebrand
trombocitopenia
trombocitose
leucopenia
leucocitose
neutropenia
eosinofilia
linfocitose
monocitose
policitemia
linfoma
leucemia
mieloma múltiplo
síndrome mielodisplásica
transtorno mieloproliferativo
esplenomegalia
adenopatia
linfadenopatia
timomegalia
imunodeficiência
aids
hiv
síndrome de imunodeficiência adquirida
infecção oportunista
pneumonia por pneumocystis
toxoplasmose cerebral
criptococose
candidíase esofágica
sarcoma de kaposi
linfoma não hodgkin
tuberculose extrapulmonar
micobacteriose
infecção por citomegalovírus
infecção por herpes vírus
hepatite viral
hepatite a
hepatite b
hepatite c
hepatite d
hepatite e
cirrose hepática
hepatite alcoólica
esteatose hepática
fibrose hepática
hipertensão portal
varizes esofágicas
encefalopatia hepática
síndrome hepatorrenal
câncer de fígado
adenoma hepático
hemangioma hepático
coledocolitíase
colangite
colangiocarcinoma
câncer de vesícula biliar
pólipo de vesícula
colecistite aguda
colecistite crônica
coledocolitíase
pancreatite aguda
pancreatite crônica
câncer de pâncreas
cisto pancreático
pseudocisto pancreático
insuficiência pancreática exócrina
diabetes pancreatogênico
gastrite aguda
gastrite crônica
úlcera gástrica
úlcera duodenal
doença do refluxo gastroesofágico
esofagite
esôfago de barrett
estenose esofágica
acalasia
divertículo esofágico
síndrome de mallory-weiss
varizes esofágicas
câncer de esôfago
câncer de estômago
linfoma gástrico
gastroparesia
síndrome de dumping
síndrome do intestino curto
má absorção
doença celíaca
intolerância à lactose
alergia alimentar
enterite
colite
proctite
apendicite aguda
diverticulose
diverticulite
doença diverticular
obstrução intestinal
íleo paralítico
vólvulo
intussuscepção
hérnia inguinal
hérnia femoral
hérnia umbilical
hérnia incisional
hérnia hiatal
câncer colorretal
pólipo colônico
síndrome de lynch
polipose adenomatosa familiar
síndrome do intestino irritável
constipação crônica
diarreia crônica
incontinência fecal
fissura anal
fístula anal
abscesso perianal
hemorroidas
prurido anal
prolapso retal
câncer de ânus
verminose
ascaridíase
ancilostomíase
enterobíase
strongiloidíase
tricuríase
teníase
cisticercose
equinococose
himenolepíase
difilobotríase
esquistossomose
fasciolíase
clonorquíase
opistorquíase
paragonimíase
fasciolopsíase
giardíase
amebíase
balantidíase
tricomoníase
leishmaniose visceral
leishmaniose tegumentar
doença de chagas
malária
babesiose
teileriose
tripanossomíase africana
toxoplasmose
criptosporidiose
isosporíase
ciclosporíase
sarcocistose
microsporidiose
pneumocistose
candidíase
aspergilose
criptococose
zigomicose
fusariose
escopulariopsose
dematiáceos
paracoccidioidomicose
histoplasmose
blastomicose
coccidioidomicose
esporotricose
cromoblastomicose
micetoma
peniciliose
geotricose
tricosporonose
malassezíase
pitiríase versicolor
tinha corporis
tinha capitis
tinha pedis
tinha unguium
tinha manuum
tinha cruris
tinha barbae
favus
queriólise pontuada
eritrasma
piedra branca
piedra negra
onicomicose
otomicose
rinossinusite fúngica
aspergiloma
micetoma pulmonar
pneumonia fúngica
fungemia
endocardite fúngica
peritonite fúngica
infecção de cateter
infecção de prótese
infecção de ferida cirúrgica
infecção de sítio cirúrgico
infecção hospitalar
infecção relacionada à assistência à saúde
infecção da corrente sanguínea
infecção do trato urinário
infecção do trato respiratório
infecção do sistema nervoso central
infecção da pele e partes moles
infecção óssea
infecção articular
infecção ocular
infecção auditiva
infecção oral
infecção gastrointestinal
infecção genital
infecção materno-fetal
infecção congênita
infecção neonatal
infecção pediátrica
infecção geriátrica
infecção em imunossuprimidos
infecção em transplantados
infecção em oncológicos
infecção em diabéticos
infecção em queimados
infecção em traumatizados
infecção em usuários de drogas
infecção em profissionais de saúde
infecção em viajantes
infecção emergente
infecção reemergente
infecção negligenciada
doença tropical
doença endêmica
doença epidêmica
doença pandêmica
doença erradicada
doença controlada
vigilância epidemiológica
notificação compulsória
investigação epidemiológica
bloqueio vacinal
quimioprofilaxia
isolamento
quarentena
distanciamento social
higienização das mãos
uso de máscaras
etiqueta respiratória
limpeza
desinfecção
esterilização
barreiras de proteção
equipamento de proteção individual
equipamento de proteção coletiva
biossegurança
gerenciamento de resíduos
acidente com material biológico
exposição ocupacional
saúde do trabalhador
ergonomia
risco ocupacional
doença ocupacional
acidente de trabalho
absenteísmo
presenteísmo
burnout
estresse ocupacional
síndrome do esgotamento profissional
assédio moral
assédio sexual
violência no trabalho
acidente de trajeto
doença relacionada ao trabalho
nexo causal
estabilidade acidentária
auxílio-doença
aposentadoria por invalidez
reabilitação profissional
readaptação funcional
retorno ao trabalho
afastamento do trabalho"""

mesh_terms = """anatomy
physiology
pathology
pharmacology
epidemiology
etiology
diagnosis
therapeutics
prophylaxis
immunology
microbiology
virology
parasitology
genetics
oncology
cardiology
neurology
psychiatry
pediatrics
geriatrics
obstetrics
gynecology
ophthalmology
dermatology
orthopedics
urology
nephrology
gastroenterology
endocrinology
hematology
rheumatology
pulmonology
infectious diseases
public health
sanitation
toxicology
radiology
biochemistry
biophysics
biostatistics
bioethics
biosafety
biotechnology
genomics
proteomics
metabolomics
transcriptomics
microbiome
resistome
zoonosis
vector
host
pathogen
antigen
antibody
vaccine
serum
antibiotic
antiviral
antifungal
chemotherapeutic
placebo
clinical trial
randomized
double-blind
cohort
case-control
cross-sectional
meta-analysis
systematic review
odds ratio
relative risk
incidence
prevalence
morbidity
mortality
lethality
survival
prognosis
pathophysiology
semiology
anamnesis
physical examination
diagnostic hypothesis
therapeutic management
evolution
discharge
death
necropsy
histopathology
cytopathology
immunohistochemistry
molecular biology
pcr
sequencing
crispr
cloning
transgenic
knockout
transcription
translation
replication
mutation
polymorphism
epigenetics
apoptosis
necrosis
autophagy
cell signaling
receptor
ligand
enzyme
substrate
inhibitor
agonist
antagonist
pharmacokinetics
pharmacodynamics
bioavailability
half-life
clearance
distribution
metabolism
excretion
toxicity
adverse effect
drug interaction
contraindication
precaution
posology
route of administration
pharmaceutical form
active ingredient
excipient
vehicle
stabilizer
preservative
cysticercosis
schistosomiasis
neurocysticercosis
taenia solium
schistosoma mansoni
leishmania braziliensis
plasmodium falciparum
ascaris lumbricoides
enterobius vermicularis
strongyloides stercoralis
hookworm infection
filariasis
leptospirosis
leprosy
tuberculosis
malaria
dengue
zika
chikungunya
yellow fever
rabies
tetanus
botulism
gangrene
sepsis
septic shock
renal failure
hepatic failure
heart failure
acute myocardial infarction
stroke
thrombosis
embolism
varicose veins
hemorrhoids
peptic ulcer
gastritis
hepatitis
cirrhosis
choledocholithiasis
pancreatitis
appendicitis
diverticulitis
hernia
intestinal obstruction
inflammatory bowel disease
crohn's disease
ulcerative colitis
irritable bowel syndrome
constipation
diarrhea
dyspepsia
nausea
vomiting
hematemesis
melena
jaundice
ascites
splenomegaly
hepatomegaly
cholelithiasis
nephrolithiasis
kidney stone
urinary tract infection
pyelonephritis
glomerulonephritis
nephrotic syndrome
nephritic syndrome
proteinuria
hematuria
leukocyturia
bacteriuria
urethritis
cystitis
prostatitis
orchitis
epididymitis
hydrocele
varicocele
phimosis
paraphimosis
cryptorchidism
hypospadias
epispadias
prostate cancer
bladder cancer
kidney cancer
testicular cancer
penile cancer
male infertility
erectile dysfunction
premature ejaculation
menopause
andropause
osteoporosis
arthritis
arthrosis
lupus
fibromyalgia
sjogren's syndrome
scleroderma
polymyositis
dermatomyositis
vasculitis
gout
pseudogout
chondrocalcinosis
bursitis
tendinitis
tenosynovitis
carpal tunnel syndrome
epicondylitis
frozen shoulder
kyphosis
scoliosis
lordosis
spondylitis
spondylosis
herniated disc
sciatica
low back pain
neck pain
chest pain
fracture
dislocation
sprain
strain
contusion
wound
burn
frostbite
insect bite
venomous animal bite
poisoning
intoxication
overdose
allergy
anaphylaxis
urticaria
angioedema
eczema
dermatitis
psoriasis
acne
rosacea
vitiligo
melasma
alopecia
hirsutism
onychomycosis
tinea
impetigo
cellulitis
abscess
furuncle
carbuncle
erysipelas
necrotizing fasciitis
myositis
rhabdomyolysis
compartment syndrome
pressure ulcer
venous ulcer
arterial ulcer
diabetic ulcer
diabetic foot
diabetic gangrene
diabetic retinopathy
diabetic neuropathy
diabetic nephropathy
type 1 diabetes
type 2 diabetes
gestational diabetes
prediabetes
hypoglycemia
hyperglycemia
diabetic ketoacidosis
hyperosmolar state
obesity
overweight
malnutrition
cachexia
anorexia
bulimia
eating disorder
vitamin deficiency
mineral deficiency
anemia
iron deficiency anemia
megaloblastic anemia
sickle cell anemia
thalassemia
hemophilia
von willebrand disease
thrombocytopenia
thrombocytosis
leukopenia
leukocytosis
neutropenia
eosinophilia
lymphocytosis
monocytosis
polycythemia
lymphoma
leukemia
multiple myeloma
myelodysplastic syndrome
myeloproliferative disorder
splenomegaly
adenopathy
lymphadenopathy
thymomegaly
immunodeficiency
aids
hiv
acquired immunodeficiency syndrome
opportunistic infection
pneumocystis pneumonia
cerebral toxoplasmosis
esophageal candidiasis
kaposi's sarcoma
non-hodgkin lymphoma
extrapulmonary tuberculosis
mycobacteriosis
cytomegalovirus infection
herpes virus infection
viral hepatitis
hepatitis a
hepatitis b
hepatitis c
hepatitis d
hepatitis e
liver cirrhosis
alcoholic hepatitis
hepatic steatosis
hepatic fibrosis
portal hypertension
esophageal varices
hepatic encephalopathy
hepatorenal syndrome
liver cancer
hepatic adenoma
hepatic hemangioma
choledocholithiasis
cholangitis
cholangiocarcinoma
gallbladder cancer
gallbladder polyp
acute cholecystitis
chronic cholecystitis
choledocholithiasis
acute pancreatitis
chronic pancreatitis
pancreatic cancer
pancreatic cyst
pancreatic pseudocyst
exocrine pancreatic insufficiency
pancreatogenic diabetes
acute gastritis
chronic gastritis
gastric ulcer
duodenal ulcer
gastroesophageal reflux disease
esophagitis
barrett's esophagus
esophageal stricture
achalasia
esophageal diverticulum
mallory-weiss syndrome
esophageal varices
esophageal cancer
stomach cancer
gastric lymphoma
gastroparesis
dumping syndrome
short bowel syndrome
malabsorption
celiac disease
lactose intolerance
food allergy
enteritis
colitis
proctitis
acute appendicitis
diverticulosis
diverticulitis
diverticular disease
intestinal obstruction
paralytic ileus
volvulus
intussusception
inguinal hernia
femoral hernia
umbilical hernia
incisional hernia
hiatal hernia
colorectal cancer
colonic polyp
lynch syndrome
familial adenomatous polyposis
irritable bowel syndrome
chronic constipation
chronic diarrhea
fecal incontinence
anal fissure
anal fistula
perianal abscess
hemorrhoids
anal pruritus
rectal prolapse
anal cancer
helminthiasis
ascariasis
hookworm infection
enterobiasis
strongyloidiasis
trichuriasis
taeniasis
cysticercosis
echinococcosis
hymenolepiasis
diphyllobothriasis
schistosomiasis
fascioliasis
clonorchiasis
opisthorchiasis
paragonimiasis
fasciolopsiasis
giardiasis
amebiasis
balantidiasis
trichomoniasis
visceral leishmaniasis
cutaneous leishmaniasis
chagas disease
malaria
babesiosis
theileriosis
african trypanosomiasis
toxoplasmosis
cryptosporidiosis
isosporiasis
cyclosporiasis
sarcocystosis
microsporidiosis
pneumocystosis
candidiasis
aspergillosis
cryptococcosis
zygomycosis
fusariosis
scopulariopsosis
dematiaceous fungi
paracoccidioidomycosis
histoplasmosis
blastomycosis
coccidioidomycosis
sporotrichosis
chromoblastomycosis
mycetoma
penicilliosis
geotrichosis
trichosporonosis
malasseziasis
pityriasis versicolor
tinea corporis
tinea capitis
tinea pedis
tinea unguium
tinea manuum
tinea cruris
tinea barbae
favus
pitted keratolysis
erythrasma
white piedra
black piedra
onychomycosis
otomycosis
fungal rhinosinusitis
aspergilloma
pulmonary mycetoma
fungal pneumonia
fungemia
fungal endocarditis
fungal peritonitis
catheter infection
prosthetic infection
surgical wound infection
surgical site infection
nosocomial infection
healthcare-associated infection
bloodstream infection
urinary tract infection
respiratory tract infection
central nervous system infection
skin and soft tissue infection
bone infection
joint infection
ocular infection
auditory infection
oral infection
gastrointestinal infection
genital infection
maternal-fetal infection
congenital infection
neonatal infection
pediatric infection
geriatric infection
infection in immunocompromised
infection in transplant recipients
infection in cancer patients
infection in diabetics
infection in burn victims
infection in trauma patients
infection in drug users
infection in healthcare workers
infection in travelers
emerging infection
reemerging infection
neglected infection
tropical disease
endemic disease
epidemic disease
pandemic disease
eradicated disease
controlled disease
epidemiological surveillance
compulsory notification
epidemiological investigation
vaccine blockade
chemoprophylaxis
isolation
quarantine
social distancing
hand hygiene
mask wearing
respiratory etiquette
cleaning
disinfection
sterilization
protection barriers
personal protective equipment
collective protection equipment
biosafety
waste management
biological material accident
occupational exposure
worker's health
ergonomics
occupational risk
occupational disease
work accident
absenteeism
presenteeism
burnout
occupational stress
professional exhaustion syndrome
moral harassment
sexual harassment
workplace violence
commuting accident
work-related illness
causal link
accident stability
sickness benefit
disability retirement
vocational rehabilitation
functional readaptation
return to work
leave from work"""

ai_ml_pt = """inteligência artificial
aprendizado de máquina
machine learning
deep learning
rede neural
backpropagation
dataset
datasets
embedding
embeddings
epoch
epochs
fine-tuning
hallucination
alucinação
inferência
token
tokens
tokenização
transformer
transformers
overfitting
underfitting
bias
viés
prompt
prompts
llm
llms
modelo de linguagem
pesos
dropout
batch
minibatch
stochastic
gradiente
otimizador
adam
sgd
pipeline
pipelines
deploy
latência
throughput
api
apis
webhook
json
yaml
vector
vetorização
rag
retrieval
generation
chain
chains
agent
agents
autônomo
pré-treinado
pretrained
zero-shot
few-shot
chain-of-thought
logits
ablação
latent space
hiperparâmetros"""

ai_ml_en = """artificial intelligence
machine learning
deep learning
neural network
backpropagation
dataset
datasets
embedding
embeddings
epoch
epochs
fine-tuning
fine-tune
hallucination
hallucinations
inference
token
tokens
tokenization
tokenize
transformer
transformers
overfitting
underfitting
bias
biases
prompt
prompts
llm
llms
large language model
weights
dropout
batch
minibatch
stochastic
gradient
descent
optimizer
adam
sgd
backend
frontend
pipeline
pipelines
deploy
deployment
latency
throughput
api
apis
webhook
webhooks
json
yaml
vector
vectors
vectorization
rag
retrieval
augmentation
generation
chain
chains
agent
agents
autonomous
fine-tuned
pretrained
zero-shot
few-shot
chain-of-thought
logits
ablation
latent space
hyperparameters"""

# Salvando arquivos de dados
with open(os.path.join(ROOT_DIR, "data/pt-BR/decs_biology_terms.txt"), "w", encoding="utf-8") as f:
    f.write(decs_terms.strip() + "\n")

with open(os.path.join(ROOT_DIR, "data/en-US/mesh_biology_terms.txt"), "w", encoding="utf-8") as f:
    f.write(mesh_terms.strip() + "\n")

with open(os.path.join(ROOT_DIR, "data/pt-BR/ai_ml_terms.txt"), "w", encoding="utf-8") as f:
    f.write(ai_ml_pt.strip() + "\n")

with open(os.path.join(ROOT_DIR, "data/en-US/ai_ml_terms.txt"), "w", encoding="utf-8") as f:
    f.write(ai_ml_en.strip() + "\n")

# Criar arquivos .aff padrão básicos se não existirem
pt_aff = os.path.join(ROOT_DIR, "data/pt-BR/pt_BR.aff")
if not os.path.exists(pt_aff):
    with open(pt_aff, "w", encoding="utf-8") as f:
        f.write("SET UTF-8\n")

en_aff = os.path.join(ROOT_DIR, "data/en-US/en_US.aff")
if not os.path.exists(en_aff):
    with open(en_aff, "w", encoding="utf-8") as f:
        f.write("SET UTF-8\n")

print("Arquivos de dados criados.")

# ==========================================
# 2. SCRIPTS PYTHON
# ==========================================

build_script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal de construção da extensão.
Lê termos locais + taxonomia, gera .dic e empacota .oxt.
"""
import os
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
INPUT_TAX = ROOT / "input" / "taxonomy"
DATA_PT = ROOT / "data" / "pt-BR"
DATA_EN = ROOT / "data" / "en-US"
OUTPUT = ROOT / "output"
TEMPLATES = ROOT / "templates"

def load_words_from_txt(folder):
    words = set()
    if not folder.exists(): return words
    for f in folder.glob("*.txt"):
        with open(f, "r", encoding="utf-8") as file:
            for line in file:
                w = line.strip().lower()
                if w and not w.startswith("#"):
                    words.add(w)
    return words

def load_words_from_dic(folder):
    words = set()
    if not folder.exists(): return words
    for f in folder.glob("*.dic"):
        with open(f, "r", encoding="utf-8", errors="ignore") as file:
            for i, line in enumerate(file):
                line = line.strip()
                if not line:
                    continue
                # Pula primeira linha (contador) se for número
                if i == 0 and line.isdigit():
                    continue
                if "/" in line:
                    line = line.split("/")[0].strip()
                if line.startswith(("#", "-", "http", "Version", "License", "Check out")):
                    continue
                w = line.lower()
                if w:
                    words.add(w)
    return words

def build_lang(lang_code, data_folder, output_name):
    print(f"Processando {lang_code}...")
    words = set()
    
    # 1. Termos locais (IA + Biologia)
    words.update(load_words_from_txt(data_folder))
    
    # 2. Taxonomia (se existir)
    words.update(load_words_from_dic(INPUT_TAX))
    
    sorted_words = sorted(words)
    
    # Salvar .dic
    dic_path = OUTPUT / f"{output_name}.dic"
    with open(dic_path, "w", encoding="utf-8") as f:
        f.write(f"{len(sorted_words)}\\n")
        for w in sorted_words:
            f.write(f"{w}\\n")
    print(f"  -> {len(sorted_words)} palavras em {dic_path}")
    
    # Copiar .aff (procura em data_folder, input ou cria fallback básico)
    source_aff = data_folder / f"{lang_code}.aff"
    if not source_aff.exists():
        source_aff = ROOT / "input" / f"{lang_code}.aff"
    if not source_aff.exists():
        affs = list(ROOT.glob("input/*.aff")) + list(data_folder.glob("*.aff"))
        source_aff = affs[0] if affs else None
    
    dest_aff = OUTPUT / f"{output_name}.aff"
    if source_aff and source_aff.exists():
        shutil.copy(source_aff, dest_aff)
        print(f"  -> Copiado {source_aff.name} para {dest_aff}")
    else:
        with open(dest_aff, "w", encoding="utf-8") as aff_f:
            aff_f.write("SET UTF-8\\n")
        print(f"  -> AVISO: Nenhum .aff encontrado para {lang_code}. Gerado .aff padrão em {dest_aff}")

def create_oxt():
    print("Criando pacote .oxt...")
    oxt_path = ROOT / "Dicionario_Cientifico_Abrangente.oxt"
    
    with zipfile.ZipFile(oxt_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona arquivos gerados (.dic e .aff)
        for f in OUTPUT.glob("*"):
            if f.is_file():
                zipf.write(f, f.name)
        
        # Adiciona templates e manifesto
        if (TEMPLATES / "dictionaries.xcu").exists():
            zipf.write(TEMPLATES / "dictionaries.xcu", "dictionaries.xcu")
        if (TEMPLATES / "description.xml").exists():
            zipf.write(TEMPLATES / "description.xml", "description.xml")
        manifest_file = TEMPLATES / "META-INF" / "manifest.xml"
        if manifest_file.exists():
            zipf.write(manifest_file, "META-INF/manifest.xml")
        
    print(f"Extensão criada: {oxt_path}")

if __name__ == "__main__":
    OUTPUT.mkdir(exist_ok=True)
    
    build_lang("pt_BR", DATA_PT, "pt_BR_scientific")
    build_lang("en_US", DATA_EN, "en_US_scientific")
    
    create_oxt()
    print("\\n✅ Build concluído com sucesso!")
'''

fetch_script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script opcional para baixar termos adicionais de APIs públicas (se disponível).
Atualmente foca nos arquivos locais e na taxonomia offline.
"""
print("Este script é um placeholder para futuras expansões via API.")
print("O build principal já utiliza os arquivos locais e a taxonomia GBIF/DeCS.")
'''

with open(os.path.join(ROOT_DIR, "src/build_extension.py"), "w", encoding="utf-8") as f:
    f.write(build_script.strip() + "\n")

with open(os.path.join(ROOT_DIR, "src/fetch_official_terms.py"), "w", encoding="utf-8") as f:
    f.write(fetch_script.strip() + "\n")

print("Scripts Python criados.")

# ==========================================
# 3. TEMPLATES XML
# ==========================================

dict_xcu = '''<?xml version="1.0" encoding="UTF-8"?>
<oor:component-data xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" oor:name="Linguistic" oor:package="org.openoffice.Office">
    <node oor:name="ServiceManager">
        <node oor:name="Dictionaries">
            <node oor:name="HunSpellDic_pt_BR_Scientific" oor:op="fuse">
                <prop oor:name="Locations" oor:type="oor:string-list">
                    <value>%origin%/pt_BR_scientific.aff %origin%/pt_BR_scientific.dic</value>
                </prop>
                <prop oor:name="Format" oor:type="xs:string">
                    <value>DICT_SPELL</value>
                </prop>
                <prop oor:name="Locales" oor:type="oor:string-list">
                    <value>pt-BR</value>
                </prop>
            </node>
            <node oor:name="HunSpellDic_en_US_Scientific" oor:op="fuse">
                <prop oor:name="Locations" oor:type="oor:string-list">
                    <value>%origin%/en_US_scientific.aff %origin%/en_US_scientific.dic</value>
                </prop>
                <prop oor:name="Format" oor:type="xs:string">
                    <value>DICT_SPELL</value>
                </prop>
                <prop oor:name="Locales" oor:type="oor:string-list">
                    <value>en-US</value>
                </prop>
            </node>
        </node>
    </node>
</oor:component-data>
'''

desc_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<description xmlns="http://openoffice.org/extensions/description/2006"
             xmlns:d="http://openoffice.org/extensions/description/2006"
             xmlns:xlink="http://www.w3.org/1999/xlink">
    <identifier value="org.cientific.dictionary.br"/>
    <version value="1.0.0"/>
    <display-name>
        <name lang="pt-BR">Dicionário Científico Abrangente (DeCS/MeSH + IA)</name>
        <name lang="en-US">Comprehensive Scientific Dictionary (DeCS/MeSH + AI)</name>
    </display-name>
    <platform value="all"/>
    <dependencies>
        <OpenOffice.org-minimal-version value="3.0" d:name="OpenOffice.org 3.0"/>
    </dependencies>
</description>
'''

manifest_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE manifest:manifest PUBLIC "-//OpenOffice.org//DTD Manifest 1.0//EN" "Manifest.dtd">
<manifest:manifest xmlns:manifest="http://openoffice.org/2001/manifest">
    <manifest:file-entry manifest:media-type="application/vnd.sun.star.configuration-data" manifest:full-path="dictionaries.xcu"/>
    <manifest:file-entry manifest:media-type="application/vnd.sun.star.package-bundle-description" manifest:full-path="description.xml"/>
</manifest:manifest>
'''

with open(os.path.join(ROOT_DIR, "templates/dictionaries.xcu"), "w", encoding="utf-8") as f:
    f.write(dict_xcu.strip() + "\n")

with open(os.path.join(ROOT_DIR, "templates/description.xml"), "w", encoding="utf-8") as f:
    f.write(desc_xml.strip() + "\n")

with open(os.path.join(ROOT_DIR, "templates/META-INF/manifest.xml"), "w", encoding="utf-8") as f:
    f.write(manifest_xml.strip() + "\n")

print("Templates XML criados.")

# ==========================================
# 4. README E GITIGNORE
# ==========================================

readme = '''# Dicionário Científico Abrangente para LibreOffice

Este repositório contém os arquivos fonte para gerar uma extensão (.oxt) do LibreOffice/WPS Office que adiciona suporte a termos científicos, médicos, biológicos e de Inteligência Artificial aos idiomas **Português (Brasil)** e **Inglês (EUA)**.

## 🚫 O Problema
Dicionários científicos existentes frequentemente obrigam o usuário a mudar o idioma do texto para "Latim" (la) para que os termos técnicos sejam aceitos. Isso desativa a correção gramatical do idioma real (pt-BR ou en-US), quebrando a verificação de concordância e pontuação.

## ✅ A Solução
Esta extensão injeta os termos técnicos como complementos válidos dos idiomas nativos `pt-BR` e `en-US`. O LibreOffice usa o dicionário padrão **E** este dicionário científico simultaneamente.

## 📦 O Que Está Incluído
- **Termos de IA/ML**: Fine-tuning, hallucination, transformer, rag, etc.
- **Termos Biomédicos**: Baseados no DeCS (Português) e MeSH (Inglês), incluindo doenças parasitológicas (cisticercose, esquistossomose), anatomia, farmacologia, etc.
- **Taxonomia**: Suporte para nomes científicos de espécies (se arquivos de taxonomia forem fornecidos).

## 🛠️ Como Gerar a Extensão

### Pré-requisitos
- Python 3.x instalado.
- Arquivos `.aff` originais do LibreOffice (`pt_BR.aff` e `en_US.aff`). Você pode extraí-los de uma instalação existente do LibreOffice ou de extensões oficiais.

### Passos

1. **Prepare os Arquivos de Entrada**:
   - Coloque seus arquivos `.aff` do LibreOffice na pasta `data/` ou `input/` (ex: `data/pt-BR/pt_BR.aff`).
   - (Opcional) Se tiver arquivos de taxonomia grandes (.dic), coloque-os em `input/taxonomy/`.

2. **Execute o Script de Build**:
   ```bash
   python src/build_extension.py
   ```
3. **Instale a Extensão:**
   - O script gerará o arquivo `Dicionario_Cientifico_Abrangente.oxt` na raiz.
   - No LibreOffice, vá em Ferramentas > Gerenciador de Extensões.
   - Clique em Adicionar, selecione o arquivo .oxt e instale.
   - Reinicie o LibreOffice.

### 📁 Estrutura do Projeto

   - `data/`: Listas de termos em texto puro (IA, Biologia) e arquivos `.aff`.
   - `src/`: Scripts Python para processamento e empacotamento.
   - `templates/`: Arquivos XML de configuração da extensão.
   - `output/`: Pasta temporária onde os dicionários finais são gerados.

### 📄 Licença
    MIT License.
'''

gitignore = '''__pycache__/
*.pyc
*.oxt
*.zip
output/
.venv/
.DS_Store
'''

readme_path = os.path.join(ROOT_DIR, "README.md")
if not os.path.exists(readme_path) or os.path.getsize(readme_path) == 0:
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme.strip() + "\n")
with open(os.path.join(ROOT_DIR, ".gitignore"), "w", encoding="utf-8") as f:
    f.write(gitignore.strip() + "\n")
print("README e .gitignore criados.")

# ==========================================
# 5. INICIALIZAÇÃO GIT
# ==========================================

import subprocess
try:
    if not os.path.exists(os.path.join(ROOT_DIR, ".git")):
        subprocess.run(["git", "init"], check=True, cwd=ROOT_DIR)
        print("\n✅ Repositório Git inicializado!")

    subprocess.run(["git", "add", "."], check=True, cwd=ROOT_DIR)

    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=ROOT_DIR)
    if status.stdout.strip():
        subprocess.run(["git", "commit", "-m", "feat: Initial commit com estrutura completa de recuperação"], check=True, cwd=ROOT_DIR)
        print("✅ Commit realizado com sucesso!")
    else:
        print("ℹ️ Nenhuma alteração pendente para commit.")

    print("\nPróximo passo: Configure o remote e faça o push se necessário:")
    print(f"   cd {ROOT_DIR}")
    print("   git remote add origin https://github.com/hugodepaula/cientific-dictionary.git")
    print("   git push -u origin main --force")
except Exception as e:
    print(f"\n⚠️ Erro na operação Git: {e}")
    print("Você pode inicializar ou comitar manualmente depois.")
print("\n🎉 RECUPERAÇÃO CONCLUÍDA! Todos os arquivos foram gerados.")
