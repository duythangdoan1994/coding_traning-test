import pandas as pd

df = pd.read_csv("data.csv")
df['_source.description_editor'] = df['_source.description_editor'].str.replace("<p>","")
df['_source.description_editor'] = df['_source.description_editor'].str.replace("</p>",":")

# df.pop("_id")
# df.pop("_source.version")
# df.pop("_source.curriculums.title")
# df.pop("_source.user.instructor_profile.description")
# df.pop("_source.image")
# df.pop("_source.lang")
# df.pop("_source.level")
# df.pop("_type")
# df.pop("_source.enabled")
# df.to_csv("data.csv")
df.to_csv("real_data.csv")