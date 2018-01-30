def pickAndShow():
  myFile = pickAFile()
  Antelope = makePicture(myFile)
  show(Antelope)
def pickAndPlay():
  myFile = pickAFile()
  AntelopeCall = makeSound(myFile)
  play(AntelopeCall)
