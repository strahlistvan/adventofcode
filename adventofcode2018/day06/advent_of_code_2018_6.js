var fs = require('fs');
var path = process.cwd();
var buffer = fs.readFileSync(path + "\\input_06_test.txt");
var input = buffer.toString().trim();

var arr = input.split("\n");

var dangerCoords = arr.map( (str, index) => { 
    return { 
        id: index + 1,
        x:  parseInt(str.split(",")[0]),
        y:  parseInt(str.split(",")[1]) 
    }    
});

console.log(dangerCoords);

function distance(point1, point2) {
    return Math.abs(point1.x - point2.x)
         + Math.abs(point1.y - point2.y);
}

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

var rectangle = createMatrix(10,10);

for (var i=0; i<rectangle.length; ++i) {
    for (var j=0; j<rectangle[i].length; ++j) {
        var point = {x: j, y: i};
        var dangerDist = dangerCoords.map(dpoint => {
            return { id: dpoint.id,
                    distance: distance(dpoint, point) 
                   };
        } ).sort((a,b) => { return a.distance > b.distance } );
    
      //  console.log(dangerDist);
        var minDist = dangerDist[0];
        var hasEqual = dangerDist[0].distance === dangerDist[1].distance;
        
        console.log("closest from "+i+","+j 
        + " = " + minDist.distance + "id = " + minDist.id);
        if (minDist.distance !== 0 && !hasEqual) {
            rectangle[i][j] = minDist.id;
        }    
    }
}
//console.log(rectangle[90][325]);

function isInfiniteField(dangerId){
    var width = rectangle.length - 1;
    var height = rectangle[0].length - 1;

    for (var i=0; i<width; ++i) {
        if (rectangle[i][0] === dangerId || rectangle[i][height] === dangerId) {
            return true;
        }
    }
    for (var i=0; i<height; ++i) {
        if (rectangle[0][i] === dangerId || rectangle[width][i] === dangerId) {
            return true;
        }
    }
    return false;    
}
var results = Array(dangerDist.length+1).fill(0);
console.log(dangerDist);

for (var i=0; i<rectangle.length; ++i) {
    for (var j=0; j<rectangle[i].length; ++j) {
        if (rectangle[i][j] != 0 && !isInfiniteField(rectangle[i][j])) {
            results[rectangle[i][j]]++;
        }
    }
}

console.log(results.sort()[0]+1);