namespace HandyApi.Models
{
    public class AxAddress
    {
        public AxAddress()
        {
            Company = "Company A";
            Country = "Country A";
            Number = "Number A";
            PhoneNumber = "PhoneNumber A";
            PostalCode = "Postal Code A";
            Street = "Street A";
        }

        public string Street { get; set; }
        public string Number { get; set; }
        public string PostalCode { get; set; }
        public string Company { get; set; }
        public string Country { get; set; }
        public string PhoneNumber { get; set; }
    }
}