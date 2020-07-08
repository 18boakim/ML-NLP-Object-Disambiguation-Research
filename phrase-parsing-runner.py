from natural_language_processor import relatePhrase
from relation_grapher import graphRelations

phraseList = ["the sphere to the right of the pyramid next to the cylinder",
              "the clamp next to the hammer on the table", "the cube", "the pyramid",
              "the front left sphere", "the back right pyramid", "the red cube", "the blue sphere",
              "the highest pyramid", "the farthest cube", "the sphere on the bottom",
              "the cube in front", "the cube above the cylinder", "the sphere in front of the cube",
              "the rightmost sphere", "the top pyramid", "the cube on the bottom",
              "the cylinder to the right", "the sphere right of the pyramid next to the cylinder",
              "the sphere right of the pyramid and next to the cylinder", "the cylinder to my left",
              "the cylinder to the robot's left", "the cylinder to your left", "the small cube",
              "the large box", "the pyramid on top of the cube", "the pyramid next to the box",
              "the sphere against the box", "the cylinder between the sphere and the pyramid on the left",
              "the cylinder next to the boxes", "the sphere in front of the cylinders",
              "the leftmost yellow cylinder", "the blue right sphere", "the yellow cube to the far right",
              "the blue cylinder on top", "the yellow cube above the blue sphere",
              "the blue sphere left of the yellow cube", "the yellow cube in the back",
              "the blue sphere to the left", "the cube behind the sphere and on the table",
              "the cube behind the sphere right of the box", "the yellow cylinder on my right",
              "the yellow pyramid on the robot's left", "the blue sphere to the robot's right",
              "the sphere in front of the blue cylinders", "the cube below the pyramids",
              "the blue leftmost cylinder in the front", "the right pyramid in back",
              "the yellow rightmost cylinder below the pyramid", "the front cube on the left",
              "the yellow top right cube", "the topmost yellow pyramid left of the cube",
              "the blue cylinder on the leftmost box", "the topmost cube on the box in the back",
              "the leftmost sphere in front next to the cylinder",
              "the pyramid on top of the cube right of the sphere on the box",
              "the pyramid on top of the cube right of the sphere and on the box",
              "the pyramid on top of the cube that's on the box and right of the sphere next to the cylinder which is on the box",
              "the pyramid on top of the cube that's on the box and right of the sphere next to the cylinder on the box",
              "the blue cylinder behind the yellow sphere and on the box to the left",
              "the blue cylinder to the left behind the yellow sphere and on the left box",
              "the yellow cylinder in front of the blue sphere below the pyramid on the box to the right",
              "the yellow cube under a yellow pyramid",
              "the pyramid that's resting on top of one of the cardboard boxes between the cylinder and the cube",
              "the yellow cylinder in between the two large cardboard boxes",
              "the yellow cylinder shape, it is on top of the leftmost box next to the pyramid and the cube",
              "the yellow pyramid on the rightmost box it's stacked right on top of a yellow cube",
              "the blue sphere right next to the cylinder that's sitting on the rightmost box"]

# Problem children
# 53, 56, 57, 58, 59, 60, 61, 62, 66, 67
for i in range(0, len(phraseList)):
    print(phraseList[i])
    nounPhrases, relationships, nounClassifiers, semantic = relatePhrase(
        phraseList[i])
    print('Noun Phrases')
    print(nounPhrases)
    print('Relationships')
    print(relationships)
    graphRelations(nounPhrases, relationships, semantic)