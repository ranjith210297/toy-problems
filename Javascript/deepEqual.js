
function deepEqual(ob1,ob2) {
	if (ob1 === ob2) {
		return true;
	}

	else if((typeof ob1 == "object" && ob1 != null) && (typeof ob2 == "object" && ob2 != null)) {
		if(Object.keys(ob1).length != Object.keys(ob2).length)
			return false;

		for (var properties in ob1) {
			if(ob2.hasOwnProperty(properties))
			{
				if(deepEqual(ob1[properties], ob2[properties]))
					return true;
			}
			else
				return false;
		}
		return true;
	}


	else
		return false;

}

var sobj = {ranjith: "name", object: 2};
console.log(deepEqual(sobj, sobj));

console.log(deepEqual(sobj, {ran:1, object: 2}));

sobj2 = {ran:{name: "k"},object: 2}
console.log(deepEqual(sobj,sobj2));