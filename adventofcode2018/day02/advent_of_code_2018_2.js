var fs = require('fs');
var path = process.cwd();
var buffer = fs.readFileSync(path + "\\input_02.txt");
var input = buffer.toString().trim();

var arr = input.split("\n");

//part one - Find the checksum
var twiceCount = 0;
var threeTimesCount = 0;

function countLetterInWord(letter, word) {
	var regex = new RegExp(letter, "g");
	return word.match(regex).length;
}

arr.forEach(word => {
	//letter counts
	var letters = word.split("").map(function(letter) { 
		return countLetterInWord(letter, word) 
	});

	if (letters.indexOf(2) != -1) {
		++twiceCount;
	}
	if (letters.indexOf(3) != -1) {
		++threeTimesCount;
	}
});

console.log("The checksum is: "+ twiceCount*threeTimesCount);

//part two - Find the common letters which differ only one character
function getDifferingCharIndex(word1, word2) {
	var diffCharIdx = [];
	for (var i=0; i<word1.length; ++i) {
		if (word1.charAt(i) !== word2.charAt(i)) {
			diffCharIdx.push(i);
		}
	}
	return diffCharIdx;
}

for (var i=0; i<arr.length; ++i) {
	for (var j=i+1; j<arr.length; ++j) {
		var diffCharIdx = getDifferingCharIndex(arr[i], arr[j]);
		if (diffCharIdx.length == 1) {
			var result = arr[i].slice(0, diffCharIdx[0])
					   + arr[i].slice(diffCharIdx[0]+1);
			
			console.log(result);
			break;
		}
	}
}