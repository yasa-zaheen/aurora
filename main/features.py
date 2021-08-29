
features = 'Model: Canon EOS-1DX Mark II\r\nSeries: Canon EOS\r\nColour: Black\r\nType: Digital SLR\r\nMaximum Resolution:\t20.2 MP\r\nFeatures: Body Only\r\nBattery Type:\tLithium-Ion\r\nBrand: Canon'

x = features.split("\n")
features = []

for i in x:
    features.append(i.split(":"))

for i in features:
    print(f"Feature Category: {i[0]}; Specifications: {i[1]}")
