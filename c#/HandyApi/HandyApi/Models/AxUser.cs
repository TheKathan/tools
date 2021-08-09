using System.Collections.Generic;

namespace HandyApi.Models
{
    public class AxUser
    {
        public AxUser()
        {
            FirstName = "FirstName A";
            MiddleName = "MiddleName A";
            LastName = "LastName A";
            AdditionalProduct = "AdditionalProduct A";
            Address = new AxAddress();
            Currency = "EUR";
            CustomerNumber = "000000";
            DebtorGroup = 111;
            DebtorInvoice = "DebtorInvoice A";
            DeliveryCondition = "DeliveryCondition A";
            DeliveryMethod = "DeliveryMethod A";
            LineDiscount = "LineDiscount A";
            Price = "Price A";
            Segment = 000;
            SeNumber = "SeNumber A";
            SalesOrderPool = "SalesOrderPool";
            PaymentMethod = "PaymentMethod A";
            PaymentTerms = "PaymentTerms A";
            Interests = new List<string>();
            MarketingPermission = true;
            UserType = "UserType";
            Email = "Email A";
            EInvoice = "EInvoice A";
            FeeGroup = "FeeGroup A";
            VatGroup = "VatGroup A";
            Organization = new AxOrganization();
            Password = "Password A";
        }

        public string CustomerNumber { get; set; }
        public string FirstName { get; set; }
        public string MiddleName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public AxOrganization Organization { get; set; }
        public string Password { get; set; }
        public AxAddress Address { get; set; }
        public List<string> Interests { get; set; }
        public bool MarketingPermission { get; set; }
        public int Segment { get; set; }
        public string VatGroup { get; set; }
        public string Currency { get; set; }
        public string DeliveryMethod { get; set; }
        public string DeliveryCondition { get; set; }
        public int DebtorGroup { get; set; }
        public string SeNumber { get; set; }
        public string PaymentTerms { get; set; }
        public string FeeGroup { get; set; }
        public string SalesOrderPool { get; set; }
        public string Price { get; set; }
        public string LineDiscount { get; set; }
        public string AdditionalProduct { get; set; }
        public string PaymentMethod { get; set; }
        public string DebtorInvoice { get; set; }
        public string EInvoice { get; set; }
        public string UserType { get; set; }
    }
}