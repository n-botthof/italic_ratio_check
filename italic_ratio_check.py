myLayers = (Glyphs.font.selectedLayers)

targetRatio = 5  # describes the height ratio of the ratio that should be achieved e.g. 1:5 –> 5 is the targetRatio
threshHold = 0.5
nodeName = "X🤢X"

affectedGlyphs = ''

for thisLayer in myLayers:
	glyphAlreadyRecorded = False  # checks if this glyph has already been recorded in affectedGlyphs
	for path in thisLayer.shapes:
		if not hasattr(path, 'nodes'):  # checks if this glyph only contains components
			continue
		for node in path.nodes:
			if node.smooth == True:
				for offCurveNode in [node.prevNode, node.nextNode]:
					xDistance = node.position.x - offCurveNode.position.x
					yDistance = node.position.y - offCurveNode.position.y
					if xDistance == 0 or yDistance == 0:
						continue
					thisRatio = yDistance/xDistance
					if thisRatio != targetRatio and thisRatio > targetRatio - threshHold and thisRatio < targetRatio + threshHold:
						offCurveNode.name = nodeName
						if not glyphAlreadyRecorded:
							affectedGlyphs += '/' + thisLayer.parent.name 
							glyphAlreadyRecorded = True
					else:
						if offCurveNode.name == nodeName:
							offCurveNode.name = None

if affectedGlyphs == '':
	print('no errors found')
else:
	Glyphs.font.newTab(affectedGlyphs)