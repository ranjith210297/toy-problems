function countBs(string1) {
	var c = 0;
	for (let i = 0; i < string1.length; i++) {
		if (string1[i] === "B") {
			c++;
		}
	}

	return c;
}

function countChar(string2, character) {
	var c=0;
	for (let i = 0; i < string2.length; i++) {
		if (string2[i] === character) {
			c++;
		}
	}

	return c;
}

console.log(countBs("BABABA"));
console.log(countChar("Ranjith","a"));