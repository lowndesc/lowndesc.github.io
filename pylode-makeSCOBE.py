import pylode

path = "C:/tmp/DTDL/lowndesc.github.io/sconto/scobe/full/0.1/"
input_file = "SCOBE.owl"
output_file = "index.html"

html = pylode.MakeDocco(
    input_data_file=f"{path}{input_file}",
    outputformat="html",
    profile="ontdoc"
).document()
with open(f"{path}{output_file}", 'w') as writer:
    writer.write(html)