var fs = require('fs');
var path = process.cwd();
var buffer = fs.readFileSync(path + "\\input_01.txt");

var input = buffer.toString().trim();

//first part
var arr = input.split("\n").map(str => parseInt(str.trim()));

var sum = arr.reduce((sum, num) => sum + num);

console.log("The sum of frequencies is " + sum);

//second part
var allPartialSums = [];
var currentSum = 0;
var found = false;

while (!found) {
	for (var i=0; i<arr.length; ++i) {
		currentSum += arr[i];
		
		if (allPartialSums.indexOf(currentSum) != -1) {
			console.log("The first frequency reached twice is " + currentSum);
			found = true;
			break;
		}
		allPartialSums.push(currentSum);		
	}	
}
