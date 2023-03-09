// setting grid size
mapGrid = document.getElementById("mapGrid").style

const gridWidth = 9
const gridHeight = 15

mapGrid.aspectRatio = gridHeight / gridWidth
mapGrid.gridTemplateColumns = ""
mapGrid.gridTemplateRows = ""

let newWidth = ""
let newHeight = ""

for (let index = 0; index < gridHeight; index++) {
    newWidth = newWidth.concat("auto ")
}
for (let index = 0; index < gridWidth; index++) {   
    newHeight = newHeight.concat("auto ")
}

mapGrid.gridTemplateColumns = newWidth
mapGrid.gridTemplateRows = newHeight