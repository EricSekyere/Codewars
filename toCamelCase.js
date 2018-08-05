/*
function that it converts dash / underscore delimited words into camel casing.
The first word within the output should be capitalized only
if the original word was capitalized.
Example:

to_camel_case("the-stealth-warrior")# returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior")# returns "TheStealthWarrior"
*/


function toCamelCase(str) {
    var delim = str.includes('-') ? '-' : '_';
    var strArr = str.trim().split(delim);
    strArr.forEach((entry, index) => {
        if (index > 0) {
            strArr[index] = entry[0].toUpperCase() + entry.substr(1, entry.length);
        }
    });
    return strArr.join("");
}

Test.assertEquals(toCamelCase("the-stealth-warrior"), "theStealthWarrior", "Something went wrong please review your algorithm")
Test.assertNotEquals(toCamelCase("The_Stealth_Warrior"), "ThestealthWarrior", "Something went wrong please review your algorithm")
Test.assertSimilar(toCamelCase("the_Quick_brown"), "theQuickBrown", "Something went wrong please review your algorithm")
Test.expect(toCamelCase("man-kit-Tone ") == "manKitTone", "Something went wrong please review your algorithm")