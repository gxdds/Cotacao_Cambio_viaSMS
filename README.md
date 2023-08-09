# Cotação do Câmbio Via SMS

Este script utilizando a twilio juntamente do Heroku permite que SMS sejam enviados automaticamente (independentemente do script estar rodando ou não) para o número verificado com a mensagem que deseja.

A mensagem está sendo o valor de conversão do Euro para Reais em tempo real utilizando a api de cotações da awesomeapi.

Para o programa funcionar corretamente é necessário o procfile com o worker e o requirements com as libs utilizadas no seu ambiente virtual ou as que estão sendo utilizadas.

Todos devem estar na mesma pasta e é necessário dar o commit para o heroku seguindo os passos do site.

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
Clone the repository
Use Git to clone smseuro's source code to your local machine.

$ heroku git:clone -a smseuro 
$ cd smseuro
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master

após isso, o worker sendo identificado, basta ir em resources, clicar no lápis para editar a sua aplicação e colocar em ON

e, por último, adicionar o add on ADVANCED SCHEDULER e definir para dia e hora que preferir.
 
