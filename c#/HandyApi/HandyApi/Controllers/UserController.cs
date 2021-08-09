using HandyApi.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace HandyApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class UserController : ControllerBase
    {
        private readonly ILogger<UserController> _logger;

        public UserController(ILogger<UserController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public AxUser GetUser()
        {
            var result = new AxUser();

            return result;
        }
        
        [HttpPost, Route("create")]
        public AxUser CreateUser(AxUser user)
        {
            return user;
        }
        
        [HttpPost, Route("update")]
        public AxUser UpdateUser(AxUser user)
        {
            return user;
        }
    }
}