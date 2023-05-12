// this is a upggioft ig
colllllors = ["purple", "green", "orange", "white", "black"]
kke = ["7", "yes", "killessto", "tuny wallalonga"]
numbresos = [5, 6, 5, 4, 3, 7, 8, 4]


// uppgift 1
for (x of kke)
{
    console.log(x)
}


// uppgift 2
for (x of colllllors)
{
    console.log(x)
}

//uppgift 3
function totality_of_numbers(the_numrsos)
{
    le_totality = 0
    for (x of the_numrsos)
    {
        le_totality += x
    }
    return le_totality
}
totality_of_numbers(numbresos)


// extra uppgift
function make_it_two(the_numbresos)
{
    temp_numbresos = []
    for (x of the_numbresos)
    {
        temp_numbresos.push(x*2)
    }
    return temp_numbresos
}

make_it_two(numbresos)


