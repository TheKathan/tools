using System;
using Newtonsoft.Json;

namespace HandyConsole
{
    public class Program
    {
        static void Main(string[] args)
        {
            var contactRequest = new ContactRequest();
            contactRequest.Contact.Email = "gof@novicell.com";
            contactRequest.Contact.FirstName = "Goncalo";
            contactRequest.Contact.LastName = "Faria";
            var aux = JsonConvert.SerializeObject(contactRequest);
            Console.WriteLine(aux);
            Console.ReadLine();
        }

    }
}