import codecs
from google_speech import Speech
telugu_padyam="""
సిరి దా వచ్చిన వచ్చును
సలలితముగ నారికేళ సలిలము భంగిన్
సిరి దాఁ బోయిన బోవును
కరిమింగిన వెలగపండు కరణిని సుమతీ!
తాత్పర్యం: సంపద వచ్చినప్పుడు కొబ్బరికాయలోకి నీరు వచ్చిన విధంగా రమ్యంగానే ఉంటుంది. అలాగే పోయినప్పుడు ఏనుగు మింగిన వెలగపండులో గుంజు మాయమైనట్లే పోతుంది.
"""
language = "te"
speed = "1.05"
speech = Speech(telugu_padyam, language)
sox_effects = ("speed", speed)
speech.play(sox_effects)
speech.save("output.mp3")
