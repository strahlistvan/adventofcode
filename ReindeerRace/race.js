//Reindeer 'class' constructor
var Reindeer = function(name, speed, maxFlyTime, maxRestTime)
{
	this.name = name;
	this.speed = speed;
	this.maxFlyTime = this.flyTime = maxFlyTime;
	this.maxRestTime = maxRestTime;
	this.distance = 0;
	this.restTime = 0;
	this.x = this.y = 0;
	
	this.image = document.createElement("img");
	this.image.src = "deer1.png";
	this.score = 0;
	
}

Reindeer.prototype.hello = function()
{
	alert("Hello, I am "+this.name);
}

//Reindeer 'class' doAction method
Reindeer.prototype.doAction = function()
{
		if (this.flyTime > 0)
		{
		   console.log("Running! Current distance: "+this.distance+" km");
			this.distance+=this.speed;
			--this.flyTime;
			if (this.flyTime==0) //if finish flying, starting to rest
				this.restTime = 0;
		}
		else 
		{
			console.log("Resting..."+(this.maxRestTime-this.restTime)+" seconds remaining");
			++this.restTime;
			if (this.restTime == this.maxRestTime)
				this.flyTime = this.maxFlyTime;
		}
		
		//Drawing part:
		var canv = document.getElementById("canv");
		this.hideInCanvas(canv);
		var ratio = canv.width/3500; 
		this.setPos(ratio*this.distance, this.y);
		this.drawToCanvas(canv);
}

Reindeer.prototype.setPos = function(x, y)
{
	this.x = x; 
	this.y = y;
}

Reindeer.prototype.drawToCanvas = function(canv)
{
    var ctx = canv.getContext("2d");
	ctx.fillStyle = "black";
	//ctx.fillRect(this.x, this.y, canv.width/20, canv.height/20);

	 var text = this.name+" távolság: "+this.distance+"km, Pontszám: "+this.score; 
	 ctx.fillText(text ,this.x ,this.y);
	 ctx.drawImage(this.image, this.x , this.y, canv.height/15, canv.height/15);
}

Reindeer.prototype.hideInCanvas = function(canv)
{
	 var ctx = canv.getContext("2d");
	ctx.fillStyle = "white";
	ctx.fillRect(0, this.y-10, canv.width, canv.height/10);
}

function addScoreToLeaders(deers)
{
	var maxDistance = deers[0].distance;
	var leaders = [];
		
	for (var i in deers)
	{
		if (deers[i].distance == maxDistance) 	//multiple lead
		{
			leaders.push(deers[i]);
		}
		else if (deers[i].distance > maxDistance) //new leader
		{
			maxDistance =deers[i].distance;
			leaders = [];
			leaders.push(deers[i]);
		}
	}
	
	for (i in leaders)
		++leaders[i].score;
}

//Main function on load
window.onload = function() 
{

	//Set and clear canvas:
	var canv = document.getElementById("canv");
	canv.width = 0.9*window.innerWidth; 
	canv.height = 0.9*window.innerHeight;
	var ctx = canv.getContext("2d");

	ctx.fillStyle = "white";
	ctx.fillRect(0, 0, canv.width, canv.height);
	
	var deers = [];
	deers.push(new Reindeer("Vixen", 8, 8, 53));
	deers.push(new Reindeer("Blitzen", 13, 4, 49));
	deers.push(new Reindeer("Rudolp", 20, 7, 132));
	deers.push(new Reindeer("Cupid", 12, 4, 43));
	deers.push(new Reindeer("Donner", 9, 5, 38));
	deers.push(new Reindeer("Dasher", 10, 4, 37));
	deers.push(new Reindeer("Comet", 3, 37, 76));
	deers.push(new Reindeer("Prancer", 9, 12, 97));
	deers.push(new Reindeer("Dancer", 37, 1, 36));
	
	for (var i in deers)
		deers[i].setPos(10+this.distance, (++i)*canv.height/10); --i;
		
	var time = 1;
	var intVal = setInterval( function() {
		console.log("megy");
		for (var i in deers)
		{
			deers[i].doAction();
		//	deers[i].setPos(10+deers[j].distance, (++i)*canv.height/10); --i;
		//	deers[i].drawToCanvas(canv);
		}
		addScoreToLeaders(deers);
		
		++time;
		if (time == 2503)
		{
		   clearInterval(intVal);
		}
		
	}, 10);
		
}