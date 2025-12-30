def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line in lines:
        print(line)

poem = "Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night"

pin_extractor(poem)
