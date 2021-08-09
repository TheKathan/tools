using HandyApi.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace HandyApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class OrganizationController : ControllerBase
    {
        private readonly ILogger<OrganizationController> _logger;

        public OrganizationController(ILogger<OrganizationController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public AxOrganization GetOrganization()
        {
            var result = new AxOrganization();

            return result;
        }
        
        [HttpPost, Route("create")]
        public AxOrganization CreateOrganization(AxOrganization organization)
        {
            return organization;
        }
    }
}