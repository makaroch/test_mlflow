import spacy  # python -m spacy download ru_core_news_lg, pip install spacy
import pymorphy3  # pip install pymorphy2

nlp = spacy.load("ru_core_news_lg")
morph = pymorphy3.MorphAnalyzer()

text = """
В России расширены меры поддержки молодых учёных

В рамках государственной программы поддержки науки в России введены новые меры, направленные на стимулирование молодых учёных. Правительство утвердило дополнительные гранты и стипендии для исследователей в возрасте до 35 лет.

Новые инициативы включают в себя увеличение финансирования научных проектов, организацию образовательных программ и семинаров для молодых специалистов, а также создание условий для международного сотрудничества в научной сфере.

Эксперты отмечают, что такие меры помогут привлечь талантливую молодёжь в науку и способствовать развитию инновационных технологий в стране.
"""

doc = nlp(text)

# entities = [(ent.text, ent.label_) for ent in doc.ents]
entities = [ent.text for ent in doc.ents]
# print(entities)

lemmas = [morph.parse(w)[0].normal_form for w in entities]
print(lemmas)
