var fs = require('fs');
var path = process.cwd();
var buffer = fs.readFileSync(path + "\\input_03.txt");
var input = buffer.toString().trim();

var arr = input.split("\n");

function createMatrix(width, height) {
    var matrix = [];
    for(var i=0; i<height; i++) {
        matrix[i] = [];
        for(var j=0; j<width; j++) {
            matrix[i][j] = 0;
        }
    }
    return matrix;
}

var rectangle = createMatrix(1000,1000);

function fillRectangle(rectangle, coords) {   
    for (var i=coords.top; i<coords.bottom; ++i) {
       for (var j=coords.left; j<coords.right; ++j) {
               ++rectangle[i][j];
       } 
    }
}

function getCoords(line) {
    var regex = /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/g;
    var res = regex.exec(line);

    return { id:     parseInt(res[1]),
             left:   parseInt(res[2]),
             top:    parseInt(res[3]),
             right:  parseInt(res[2]) + parseInt(res[4]), 
             bottom: parseInt(res[3]) + parseInt(res[5]) };
}

//each claim in the input file
arr.forEach(line => {
    if (line) {
        var coords = getCoords(line);
        fillRectangle(rectangle, coords);
    }            
});

//calculate overlapping squares 
var squreCount = 0;
for (var i=0; i<rectangle.length; ++i) {
    for (var j=0; j<rectangle[i].length; ++j) {
        if (rectangle[i][j] > 1) {
            ++squreCount;
        }
    }
}
console.log("Square count : " + squreCount);

//part2 - check all claims - find the non-overlapping one
function hasOverlappingSqure(rectangle, coords) {   
    for (var i=coords.top; i<coords.bottom; ++i) {
       for (var j=coords.left; j<coords.right; ++j) {
               if(rectangle[i][j] !== 1) {
                   return true;
               }
       } 
    }
    return false;
}

arr.forEach(line => {
    if (line) {
        var coords = getCoords(line);
        if (!hasOverlappingSqure(rectangle, coords)) {
            console.log(coords);
            return;
        }   
    }            
});