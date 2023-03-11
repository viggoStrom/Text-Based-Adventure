// setting grid size

mapGrid = document.getElementById("mapGrid")

const gridRows = 13
const gridColumns = 15

mapGrid.style.aspectRatio = gridColumns / gridRows
mapGrid.style.gridTemplateColumns = ""
mapGrid.style.gridTemplateRows = ""

let newWidth = ""
let newHeight = ""

for (let index = 0; index < gridColumns; index++) {
    newWidth = newWidth.concat("auto ")
}
for (let index = 0; index < gridRows; index++) {
    newHeight = newHeight.concat("auto ")
}

mapGrid.style.gridTemplateColumns = newWidth
mapGrid.style.gridTemplateRows = newHeight

// \setting grid size


// populating grid

const coordinates = document.querySelector("aside p:first-of-type")
const detailsPanel = document.querySelector("#detailsPanel")

let colors = ["lightGray", "white"]
let colorBit = 1
for (let y = 0; y < gridRows; y++) {
    for (let x = 0; x < gridColumns; x++) {
        const newDiv = document.createElement("div")
        newDiv.className = "mapSquare"
        newDiv.id = `x` + x
        newDiv.id += `y` + y
        newDiv.onclick = showDetails = (event) => {
            // shows details of square

            coordinates.innerHTML = event.srcElement.id

            // \shows details of square
        }
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