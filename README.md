Leonardo Silva Amaral
================================================================================

&raquo;		E-Mail: <contato@leonardoamaral.com.br>  
&raquo;		Telefone: +55 11 91916-0254  
&raquo;		[Resume no GitHub](https://github.com/leleobhz/resume)  

O profissional
--------------------------------------------------------------------------------

Desde o primeiro contato com computadores, sempre me fascinou o funcionamento deles. A progressão do aprendizado e o interesse em sistemas Linux, na filosofia de sistemas abertos e em redes tornou-me Administrador de Sistemas.

Os anos de experiência com ambiente corporativo mostraram - e ainda mostram - um desafio constante na manutenção das telecomunicações e sistemas como plano de fundo para todos os serviços fundamentais nos negócios.

E na última experiência, a entrada no mundo dos ISP's foi determinante para maior interesse em telecomunicações e soluções livres de apoio tecnológico a negócios e serviços.

Experiências Profissionais
--------------------------------------------------------------------------------

#### &raquo; Prodabel - Processamento de Dados da Prefeitura de Belo Horizonte

&raquo;&raquo; Tempo de atuação: 2006  
&raquo;&raquo; Área de atuação: Estágio em TI
&raquo;&raquo; Atividades: Marca a primeira implementação em larga escala de sistemas com Linux: Participei paralelamente ao suporte com patches de sistema no desenvolvimento da Distribuição Linux Libertas - implementada pela prefeitura.  

#### &raquo; Comjota Consultoria de TI

&raquo;&raquo; Tempo de atuação: 2008 - Presente  
&raquo;&raquo; Área de atuação: Administração de Servidores  
&raquo;&raquo; Atividades: Implemento, administro e presto suporte nível 2 aos servidores da empresa e de seus clientes. Participo na criação de novas soluções e atendimento de demandas internas e externas.  

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

Implementei várias soluções marcantes, inusitadas e de grande impácto e compartilho algumas bastante criativas:

#### &raquo; Criação do sistema zimbrahelpdesk

&raquo;&raquo; A Santa Casa de Misericórdia de Belo Horizonte - atendida pela Comjota - reportou a necessidade de um sistema leve e em console para troca de senhas do sistema de email em caso de bloqueio por erro. Entretanto o Helpdesks não poderiam ter acesso privilégiado ao sistema de email. 

Aproveitando a disponibilidade de cliente de terminal em todas as estações, desenvolvi o zimbrahelpdesk utilizando o projeto [2502](https://github.com/caetanus/resume/blob/master/resume-pt_br.rst#2502) do desenvolvedor Marcelo Caetano - visando uma interface de console limpa com controle de acesso via PAM ao sistema de troca de senha - aprovado e implementdo pela gestão de TI.

#### &raquo; Reestruração da SCW Telecom
&raquo;&raquo; A SCW Telecom é um ISP portador do ASN 28138 na cidade de São Carlos. O provedor encontrava-se sem administrador de sistema - tendo perdido muitos clientes devido a downtimes e incidentes. 

Encontrei soluções legadas inviáveis de manter. Os servidores rodavam Slackware e alguns usavam o VirtualBox Headless como virtualizador - sem documentação nem padronização. Os acordos de Peering estavam documentados somente nas configurações do roteador de borda e foi necessária engenharia reversa das configurações para iniciar o reestabelecimento das sessões. 

Todo o maquinário crítico foi reimplementado com Gentoo Hardened - devido a manutenção dos patches de segurança Grsec e PAX com controle RBAC - e a virtualização implementada com Xen + FLask/XSM e Gentoo Hardened, respeitando a padronização dos guias da distribuição. Criei a documentação e hospedei-a em repositório Mercurial externo. Mais detalhes podem ser descritos em uma oportunidade de contato.

#### &raquo; PHP mal educado
&raquo;&raquo; Em um determinado cliente da Comjota foi reportado lentidão extrema no seu website principal, hospedado internamente no NOC do cliente.  
Averiguei altos tempos de processamento e travamentos no processamento PHP. O site estava com uma versão extremamente defasada de Wordpress com código PHP personalizado. Havia a suspeita de comprometimento dos arquivos do site.

À empresa foi recomendada a construção de um novo website em uma plataforma atualizada e com políticas eficientes de desenvolvimento, porém pelo prazo da solução proposta, solicitei um servidor dedicado nos EUA (Devido ao preço) com uma configuração respeitável e migrei o website. 

Entretanto percebido processos bloqueantes nestes códigos, exigindo migração ligeiramente diferente do convencional: Optei em manter o Apache para evitar aborrecimentos com arquivos .htaccess e implementei o módulo mod\_fcgi com o PHP processado em diversas threads alocadas on-the-fly e com o UID do usuário dono do site (Que padronizei como o FQDN do site hospedado). Preparei todo o ambiente para manter em um único lugar - de forma organizada - os arquivos de configuração do domínio relativo ao apache2 e ao php e os arquivos do website. 

O website foi migrado e os parametros do PHP ajustados para trabalhar mais confortável com o workload de cada domínio. Além do perfeito isolamento do PHP em relação ao webserver - evitando a carga de conteúdo estático e que algum código PHP mal intencionado se prolifere para outros sites ou para o sistema - implementei um sistema de proxy-cache reverso utilizando Varnish e o acesso aos desenvolvedores do site foi provido com uma solução mista de SFTP/SSH com chroot e bind mounting, provendo completo isolamento entre usuários e permitindo ao desenvolvedor introduzir mudanças nos parametros do apache2.conf e no php.ini para um fine-tuning de todo processo.

A solução visava trocar uma certa penalidade em performance (Compensada com o servidor mais potente) por escalabilidade sem precedentes, já que cada sessão do website abria em uma thread diferente e outras sessões não travam ou atrapalham, resolvendo o problema por completo. O servidor encontra-se atualmente com mais de 130 dias de uptime e mesmo após a implementação de um novo site, o servidor permanece operante e sem sobrecarga ou problemas de manutenção de configuração.

#### &raquo; Scanner em rede
&raquo;&raquo; Compartilhar impressoras em rede é muito trivial, mas e um pool de scanners? 

Em um cliente especializado em marketing, foi passada esta demanda e a mesma foi solucionada com saned + xinetd + xsane nos clientes. 

Sequer era necesário pools de compartilhamento, pendrives, PDFs ou qualquer outra solução: O scanner funcionava na estação como se estivesse local, permitindo enquadramento, escolha de formato, ajuste de imagem e qualquer outra opção que o scanner suportasse.

#### &raquo; Roteamento e gerenciamento avançado de redes
&raquo;&raquo; O primeiro trabalho em redes diferentes do perfil atual de LAN (Rede privada classe B ou C com NAT no roteador de saída e um único IP público) foi em um pequeno link de 512kbps contratado para meu uso com 8 ips.

Também configurei os roteadores de saída dos departamentos de engenharia sanitária e ambiental e de engenharia de estruturas da Universidade Federal de Minas Gerais (UFMG) - cada departamento com um /24 válido e roteavel. 

E a maior experiência em telecomunicações foi gerenciar o ASN 28138 da SCW Telecom - contendo um bloco /20 IPv4 e com um bloco /32 IPv6 em processo de implementação. Abriu-me o leque da experiência com redes LAN para redes CAN e MAN tanto em implementação com cabeamento Ethernet tanto com fibras ópticas e P2P sem fio. Desenvolvi experiencia com sistemas da Ubiquity e Mikrotik - com notavel implementação de um P2P de 9Km utilizando o AirFiber trafegando entre 200 e 500mbps em 24Ghz.
