from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("./"),
    autoescape=select_autoescape()
)

template = env.get_template("template.pine")

symbols = [
    "2983", "4173", "4174", "4175", "4176", "4177", "4178", "4179", "4180", "4192",
    "4193", "4432", "4885", "4936", "6521", "6613", "6614", "7343", "7361", "7362",
    "7363", "7367", "7368", "7698", "9327", "2933", "4498", "4194", "4196", "4888"
]

print(template.render({'symbols': symbols}))
