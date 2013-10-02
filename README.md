Leonardo Silva Amaral
================================================================================

&raquo;		E-Mail: <contato@leonardoamaral.com.br>  
&raquo;		Telefone: +55 11 91916-0254

O profissional
--------------------------------------------------------------------------------

Desde o primeiro contato com computadores, o interesse no funcionamento dessas máquinas sempre fascinou-me. Ao crescer o contato com sistemas Linux e a filosofia de sistemas abertos e pesquisáveis, tornei-me Administrador de Sistemas.

Os anos de contato com ambiente corporativo mostraram - e ainda mostram - um desafio constante na manutenção das redes e telecomunicações sempre como plano de fundo para todos os serviços fundamentais nos negócios.

E nas últimas experiências, o contato com infra-estrutura de ISP foram determinantes para o foco e interesse em telecomunicações e soluções livres de apoio tecnológico a negócios e serviços.

Este perfil demonstra minha atuação como Administrador de Redes e Sistemas.

Experiências Profissionais
--------------------------------------------------------------------------------

#### &raquo; Prodabel - Processamento de Dados da Prefeitura de Belo Horizonte

&raquo;&raquo; Tempo de atuação: 2006  
&raquo;&raquo; Área de atuação: Estágio em TI
&raquo;&raquo; Atividades: Marca o início do contato com implementações em Linux. Participou paralelamente com patches de sistema no desenvolvimento da Distribuição Linux Libertas - implementada pela prefeitura.  

#### &raquo; Comjota Consultoria de TI

&raquo;&raquo; Tempo de atuação: 2008 - Presente  
&raquo;&raquo; Área de atuação: Administração de Servidores  
&raquo;&raquo; Atividades: Implemento e administro os servidores da empresa e de seus clientes também prestando suporte de nível 2 para estas implementações. Participa da criação de novas soluções e atendimento de demandas dos clientes da empresa.  

#### &raquo; SCW Telecom - ASN 28138

&raquo;&raquo; Tempo de atuação: 2012 - Presente  
&raquo;&raquo; Área de atuação: Administração de Redes  
&raquo;&raquo; Atividades: Administração de todo o maquinário do DataCenter do provedor tal como seus serviços de rede. Atua na implementação e manutenção do AS e dos links de Trânsito e conectividade à PTTs - especialmente o PTT-Metro SP.  

Formação Acadêmica
--------------------------------------------------------------------------------

#### &raquo; Universidade de São Paulo - Instituto de Física de São Carlos

&raquo;&raquo; Tempo de atuação: 2010~2012, 2013?  
&raquo;&raquo; Curso: Física Computacional  

Certificações
--------------------------------------------------------------------------------

&raquo;&raquo; LPIC nível 2 - Identificador LPI000106747 / Código verificador hgwxf77vau  
&raquo;&raquo; Curso de IPv6 com ênfase em roteamento - Provido pelo NIC.br  
&raquo;&raquo; Curso para homologação de NR-35  
&raquo;&raquo; Curso de Infraestrutura em redes ópticas - UFSCar - São Carlos  

Experiências Técnicas
--------------------------------------------------------------------------------

  Em todas as experiências profissionais, houveram algumas soluções marcantes, inusitadas e de grande impácto nos ambientes em que elas foram implementadas e apresento as mais relevantes e criativas a seguir:

#### &raquo; Criação do sistema zimbrahelpdesk

&raquo;&raquo; A Santa Casa de Misericórdia de Belo Horizonte - atendida pela Comjota - reportou a necessidade de um sistema extremamente leve e de fácil deploy para troca de senhas do sistema de email em caso de bloqueio por erro. Entretanto o Helpdesks não poderiam ter acesso privilégiado ao sistema de email. 

Aproveitando a disponibilidade de cliente de terminal em todas as máquinas do helpdesk, desenvolvi o zimbrahelpdesk utilizando como plataforma de IPC o projeto [2502](https://github.com/caetanus/resume/blob/master/resume-pt_br.rst#2502) do desenvolvedor Marcelo Caetano, visando uma interface de console limpa e que autorizasse por PAM-Login que somente determinados usuários acessassem o sistema de troca de senha - que foi implementado e aprovado pela gestão de TI.

#### &raquo; Reestruração da SCW Telecom
&raquo;&raquo; A SCW Telecom é um ISP de pequeno porte, portador do ASN 28138 e instalado na cidade de São Carlos. O provedor encontrava-se sem administrador de sistema há muitos meses e com isso perdeu uma boa parcela de seus clientes devido a downtimes e incidentes onde não havia mais um profissional disponível. 

Ao deparar com a infra-estrutura para manter, encontrei soluções muito inviáveis de manter e muito legadas. Todas as máquinas rodavam Slackware, algumas tinham VirtualBox Headless como solução de virtualização e não havia documentação nem padronização das instalações. Os acordos de Peering entre provedores que passavam pelo PTT-Metro SP ficaram somente nas configurações do roteador de borda e foi necessária engenharia reversa das configurações para iniciar o reestabelecimento das sessões. 

Todo o maquinário crítico foi substituído por Gentoo Hardened - devido a manutenção dos patches de segurança Grsec e PAX com controle RBAC - e a virtualização implementada com Xen + FLask/XSM e Gentoo Hardened, respeitando a padronização dos guias da distribuição e construindo documentação hospedada em repositório Mercurial externo. Mais detalhes podem ser descritos em uma oportunidade de contato.

#### &raquo; PHP mal educado
&raquo;&raquo; Em um determinado cliente da Comjota foi reportado lentidão extrema no seu website principal, hospedado internamente no NOC do cliente.  
Averiguei altos tempos de processamento e muitas travadas no processamento PHP devido a versão extremamente defasada de Wordpress com código PHP customizado (e provavelmente tão antigo quanto), com possibilidade de comprometimento da segurança do website. 

À empresa foi recomendada a construção de um novo website em uma plataforma mais atualizada e com melhores políticas de desenvolvimento, porém esta solução iria demorar e desta forma, solicitei um servidor dedicado nos EUA (Devido ao preço) com uma configuração respeitável e migrei o website. 

Entretanto como eu já havia percebido que haviam processos bloqueantes nestes códigos, a migração foi feita ligeiramente diferente do convencional: Optei em manter o webserver Apache para evitar aborrecimentos desnecessários com arquivos .htaccess (Já que o sistema não era mais mantido) e implementei o módulo php-fcgi com o PHP sendo processado em diversas threads alocadas on-the-fly e com o UID do usuário dono do site (Que padronizei como o FQDN do site hospedado). Preparei todo o ambiente para montar em uma pasta um diretório "conf" para customização por-domínio do php.ini e a pasta public de onde advinha o conteúdo do site. 

O website foi migrado e os parametros do PHP ajustados para trabalhar mais confortável com o workload de cada domínio. Alem do perfeito isolamento do PHP em relação ao webserver visando enfrentar a retenção da carga de conteúdo estático e evitar que algum código PHP mal intencionado se prolifere para outros sites ou para o sistema, foi implementado um sistema de proxy-cache reverso utilizando Varnish e o acesso aos desenvolvedores do site foi provido usando um solução mixta de SFTP/SSH com chroot e bind mounting, provendo completo isolamento entre usuários também para manuteção do website e também permitindo ao desenvolvedor introduzir mudanças nos parametros do apache2.conf e no php.ini, permitindo um fine-tuning de todo processo.

A solução visava trocar uma certa penalidade em performance (Compensada com o servidor mais encorpado) por escalabilidade sem precedentes, já que cada sessão do website abria em uma thread diferente, permitindo ao servidor conter uma sessão sem atrapalhar as outras ou travar o website, resolvendo o problema por completo. O servidor encontra-se atualmente com mais de 130 dias de uptime e mesmo após a implementação de um novo site, o servidor permanece como estava e sem sobrecarga ou problemas de manutenção de configuração.

#### &raquo; Scanner em rede
&raquo;&raquo; Compartilhar impressoras em rede é muito trivial, mas e um pool de scanners? 

Em um cliente especializado em marketing, foi passada esta demanda e a mesma foi solucionada com saned + xinetd + xsane nos clientes. 

Sequer era necesário pools de compartilhamento, pendrives, PDFs ou qualquer outra solução: O scanner funcionava na estação como se estivesse local, permitindo enquadramento, escolha de formato, ajuste de imagem e qualquer outra opção que o scanner suportasse.

#### &raquo; Roteamento e gerenciamento avançado de redes
&raquo;&raquo; O primeiro contato com redes diferentes do perfil atual de LAN (Rede privada classe B ou C com NAT no roteador de saída e um único IP público) foi em um pequeno link de 512kbps contratado por mim com 8 ips disponíveis, sendo o gateway em faixa diferente dos IPs contratados. 

Alguns anos após esta experiência, configurei os roteadores de saída dos departamentos de engenharia sanitária e ambiental e de engenharia de estruturas da Universidade Federal de Minas Gerais (UFMG), onde cada departamento era portador de um bloco /24 válido e roteavel com políticas individuais de roteamento. 

Após esta experiência firmei na área de telecomunicações ao gerenciar o ASN 28138 da SCW Telecom contendo um bloco /20 IPv4 e com um bloco /32 IPv6 - em processo de implementação, abrindo o leque da experiência com redes LAN para redes CAN e MAN tanto em implementação com cabeamento Ethernet tanto com fibras ópticas e P2P sem fio, sendo experiente com sistemas da Ubiquity e Mikrotik - com notavel implementação de um Ponto a Ponto sem fio de 9Km utilizando o AirFiber da Ubiquity trafegando entre 200 e 500mbps.
