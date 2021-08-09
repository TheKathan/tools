namespace HandyApi.Models
{
    public class AxOrganization
    {
        public AxOrganization()
        {
            Name = "Organization A";
            Address = new AxAddress();
            ContactUser = null;
            Cvr = "Cvr A";
            Ean = "Ean A";
            Phone = "Phone A";
        }

        public string Name { get; set; }
        public string Cvr { get; set; }
        public string Ean { get; set; }
        public string Phone { get; set; }
        public AxAddress Address { get; set; }
        public AxUser ContactUser { get; set; }
    }
}