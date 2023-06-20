using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace WebApplication2
{
    /// <summary>
    /// Descrição resumida de WebServiceSoap
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // Para permitir que esse serviço da web seja chamado a partir do script, usando ASP.NET AJAX, remova os comentários da linha a seguir. 
    // [System.Web.Script.Services.ScriptService]
    public class WebServiceSoap : System.Web.Services.WebService
    {

        [WebMethod]
        public string Nome_RU()//primeiro método
        {
            return "Moacir Domingos da Silva Junior RU 3539252";
        }

        [WebMethod]
        public int Pitagoras(int a, int b, int c)//segundo método
        {
           
           return ((c * c) = ((a * a) + (b * b));
        }
              
    }
}
