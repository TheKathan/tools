using System.Collections.Generic;
using Newtonsoft.Json;

namespace HandyConsole
{
    public class ContactRequest
    {
        [JsonProperty("contact")]
        public Contact Contact { get; set; } =  new Contact();
    }

    public class FieldValue
    {
        [JsonProperty("field")]
        public string Field { get; set; } = string.Empty;
        [JsonProperty("value")]
        public string Value { get; set; } = string.Empty;
    }

    public class Contact
    {
        [JsonProperty("email")]
        public string Email { get; set; } = string.Empty;
        [JsonProperty("firstName")]
        public string FirstName { get; set; } = string.Empty;
        [JsonProperty("lastName")]
        public string LastName  { get; set; } = string.Empty;
        [JsonProperty("phone")]
        public string Phone { get; set; } = string.Empty;
        [JsonProperty("fieldValues")]
        public List<FieldValue> FieldValues { get; set; }  = new List<FieldValue>();
    }
}