using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula4
{
     class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Aula Prática de C# 4!");
            Console.WriteLine("----------------------------------------");


            Console.WriteLine("----------------------------------------");
            Console.WriteLine("Treads");
            Console.WriteLine("----------------------------------------");

            ThreadPing exercicio1 = new ThreadPing();
            exercicio1.StartPing();
        }
    }
}


CLASS

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.NetworkInformation;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Aula4
{
    public class ThreadPing
    {
        private string endereco = "google.com";
        int countPing = 0;
        bool executePing = false;

        public void StartPing()
        {
            Console.Write("Digite S a qualquer momento para interromper");

            var threadPingger = new Thread(ExecutePing);
            threadPingger.Start();
            executePing = true;

            var comandoSair = "S";
            var comando = string.Empty;

            while (!comandoSair.Equals(comando))
            {
                comando = Console.ReadLine();
            }

            executePing = false;

            while(threadPingger.IsAlive)
            {
                Console.WriteLine("Esperando finalizar");
            }

            Console.WriteLine("Thread finalizada");
        }

        public void ExecutePing()
        {
            while (executePing)
            {
                Ping pingger = new Ping();

                var pingResponse = pingger.Send(endereco);

                Console.WriteLine($"Ping {countPing}: {endereco} | Status: {pingResponse.Status} - {pingResponse.RoundtripTime}ms");
                countPing++;

                //espera alguns segundos
                Thread.Sleep(2000); 
            }
        }
    }
}
