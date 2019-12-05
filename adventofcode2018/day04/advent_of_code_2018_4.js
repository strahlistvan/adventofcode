var fs = require('fs');
var path = process.cwd();
var buffer = fs.readFileSync(path + "\\input_04_test.txt");
var input = buffer.toString().trim();

var arrTxt = input.split("\n");
arrTxt = arrTxt.sort();

arrObj = [];
var prevDate = null;

arrTxt.forEach(line => {
    var pattDate = /\[(\d+-\d+-\d+ \d+:\d+)\].+/;
    var date = new Date(pattDate.exec(line)[1]);
    
    arrObj.push({fullText: line,
                 date: date,
                 dateDiff: parseInt(date - prevDate) / 60000
                });

    prevDate = date;
});

var guardSleepTimes = new Object();

//Find the total longest sleeper
for (var i=0; i<arrObj.length; ++i) {

    var pattGuard = /Guard (#\d+) begins shift/;

    if (pattGuard.test(arrObj[i].fullText)) {
        var guardId = pattGuard.exec(arrObj[i].fullText)[1];

        while(arrObj[++i] && !pattGuard.test(arrObj[i].fullText) ) {
            console.log(
                guardId + " " + arrObj[i].dateDiff 
                + " min " + arrObj[i].fullText);

            if (arrObj[i].fullText.indexOf("wakes up") !== -1) {
                if (guardSleepTimes.hasOwnProperty(guardId)) {
                    console.log("Increase " + guardId + " by " + arrObj[i].dateDiff);
                    guardSleepTimes[guardId] += arrObj[i].dateDiff;
                }
                else {
                    guardSleepTimes[guardId] = arrObj[i].dateDiff;
                } 
            }      
        }
    }
}

console.log(guardSleepTimes);

//find the longest sleeper longest nap
var maxSleepLength = 0;
for (var i=0; i<arrObj.length; ++i) {

    if (arrObj[i].fullText.indexOf("#10") !== -1) {
     
        while(arrObj[++i] && !arrObj[i].fullText.indexOf("Guard") !== -1 ) {  
            if (arrObj[i].fullText.indexOf("asleep") !== -1) {
                 if (arrObj[i].dateDiff > maxSleepLength) {
                     maxSleepLength = arrObj[i].dateDiff;
                 }
            }               
        }
    }
}

console.log("Guard sleep = " + maxSleepLength);