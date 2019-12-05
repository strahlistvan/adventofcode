var fs = require('fs');
var path = process.cwd();
var buffer = fs.readFileSync(path + "\\input_05.txt");
var input = buffer.toString().trim();

//var input = "dabAcCaCBAcCcaDA";

function fullReaction(polymer) {
    var hasMoreDuplication = true;
    while (hasMoreDuplication) {
        var found = false;
        for (var i=0; i<polymer.length-1; ++i) {
            if ( polymer.charAt(i) !== polymer.charAt(i+1)
              && polymer.charAt(i).toLowerCase() === polymer.charAt(i+1).toLowerCase()) {
                  polymer = polymer.substr(0, i) + polymer.substr(i+2);
                  found = true;
              }
        }
    
        if (!found) {
            hasMoreDuplication = false;
        }
    }
    return polymer;  
}

//part one - full reaction
var output = fullReaction(input);
console.log(output);
console.log("Remaining length: " + output.length);

//part two - which unit should remove
function removeAllUnits(polymer, unit) {
    var patt = new RegExp(unit+"|"+unit.toUpperCase(), "g");
    return polymer.replace(patt, "");
}

var clearedReactedLengths = [];
for (var code = "a".charCodeAt(0); code < "z".charCodeAt(0); ++code) {

    var chr = String.fromCharCode(code);
    var cleared = removeAllUnits(input, chr);

    if (cleared.length < input.length) {
        output = fullReaction(cleared);
        console.log("Removing all " + chr 
          + "completed. Length: " + output.length);
        
        var obj = {unit : chr, count : output.length };

        clearedReactedLengths.push(obj);
    }
}

console.log(clearedReactedLengths);

