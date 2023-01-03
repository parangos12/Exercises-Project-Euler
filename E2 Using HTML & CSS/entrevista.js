for (i = 0; i <= 100;i=i+1)
{
    if (i % 3 == 0 && i % 5 == 0)
    {
        document.write(i + " is bizz buzz"+"<br>") 
    }
    else if (i % 5 == 0)
    {
        document.write(i + " is buzz\n" + "<br>")
    }
    else if (i % 3 == 0)
    {
        document.write(i + " is bizz" + "<br>")
    }
    else
    {
        document.write(i + "<br>")
    }
}