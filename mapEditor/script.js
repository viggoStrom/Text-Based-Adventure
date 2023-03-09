// setting grid size

mapGrid = document.getElementById("mapGrid")

const gridWidth = 9
const gridHeight = 15

mapGrid.style.aspectRatio = gridHeight / gridWidth
mapGrid.style.gridTemplateColumns = ""
mapGrid.style.gridTemplateRows = ""

let newWidth = ""
let newHeight = ""

for (let index = 0; index < gridHeight; index++) {
    newWidth = newWidth.concat("auto ")
}
for (let index = 0; index < gridWidth; index++) {
    newHeight = newHeight.concat("auto ")
}

mapGrid.style.gridTemplateColumns = newWidth
mapGrid.style.gridTemplateRows = newHeight

// \setting grid size

// populating grid

let colors = ["lightGray", "white"]
let colorBit = 1
for (let y = 0; y < gridWidth; y++) {
    for (let x = 0; x < gridHeight; x++) {
        let newDiv = document.createElement("div")
        newDiv.className = "mapSquare" 
        newDiv.className += ` x` + x
        newDiv.className += ` y` + y
        newDiv.style.backgroundColor = colors[colorBit]
        if (colorBit == 0) {
            colorBit = 1
        } else {
            colorBit = 0
        }
        mapGrid.appendChild(newDiv)
    }
}

// \populating grid