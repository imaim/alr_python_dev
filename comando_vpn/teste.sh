#!/bin/bash
arquivo=$(cat /gitlab/vpn-inventario/hosts)
DATA=`date +%d%m%Y`
HORA=`date +%H%M%S`
DIR_LOG=/db/backup/checklist/auditoria
# Limpa tela inicial
clear
# Funcao de Pesquisa
pesquisa_vpn () {
    if [ "$1" == "livre" ] || [ "$1" == "LIVRE" ] ; then
        # Tratativa para string com parametro LIVRE na coluna
        arquivo=$( echo -e "$arquivo" | grep -i "$1" | awk -F'#' '{print $3,$4,$5}' | tr "[:lower:]" "[:upper:]" | sed "s/ /_/g" )
    elif [[ "$1" =~ ^[0-9]+$ ]] || [[ "$1" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] || [ "$1" != "" ] ;  then
        # Tratativa para numeral
        arquivo=$( echo -e "$arquivo" | grep -i "$1" | awk -F'#' '{print $2,$3,$4}' | tr "[:lower:]" "[:upper:]" | sed "s/ /_/g" )
    else
        echo -e "\e[00;33m$coluna \e[00m"
        arquivo=$( echo -e "$arquivo" | awk -F'#' '{print $2,$3,$4}' | tr "[:lower:]" "[:upper:]")        
        echo "${arquivo}"
    fi
}

# Armazenamento em vetor para acesso e exibicao
pesquisa_exibicao () {
    
    #arquivo=$(echo -e "$arquivo"|grep '${ARGUMENT}')
    IP_CONSULTAS=()
    LINHA_CONSULTA=()
    COUNT_STOP=1
    COUNT_OK=1
    # le cada linha do resultado e incrementa ao identificar campo stop
    while read -r linha ; do

        LINHA_RESULT=$(echo -e "$linha")
        IP_LINHA=$(echo -e "$linha"| awk -F'_' '{print $1}')
        #COUNT_IP_LINHA=$(echo -e "${IP_LINHA}" |sed "s/ //g"| wc -l)
        PORTA_LINHA=$(cat /gitlab/vpn-inventario/hosts | grep -w "${IP_LINHA}"| grep "ansible_ssh_port" | awk '{print $2}' | cut -d"=" -f2)
        ## echo -e "$COUNT_STOP - $linha"
        IP_CONSULTAS+=([${COUNT_STOP}]=${IP_LINHA}-${PORTA_LINHA})

        # Limita a alimentação do vetor aos resultados considerados completos (ip e resultado incial da pesquisa)
        if [ -n "${LINHA_RESULT}" ] && [[ "${IP_LINHA}" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] ;
        then
            # tratativa de visualização em funçao da quantidade de caracteres no numero de cada resultado
            if [ ${COUNT_STOP} -lt 10 ]
            then
                coluna="N    IP_VPN          NOME_CLIENTE                                 PORTA           CLIENT"
                LINHA_CONSULTA+=([${COUNT_STOP}]=\[${COUNT_STOP}\]---${LINHA_RESULT})
            elif [ ${COUNT_STOP} -lt 100 ]
            then
                coluna="N      IP_VPN          NOME_CLIENTE                                 PORTA           CLIENT"
                LINHA_CONSULTA+=([${COUNT_STOP}]=\[${COUNT_STOP}\]--${LINHA_RESULT})
            else
                coluna="N        IP_VPN          NOME_CLIENTE                                 PORTA           CLIENT"
                LINHA_CONSULTA+=([${COUNT_STOP}]=\[${COUNT_STOP}\]--${LINHA_RESULT})
            fi
            ((COUNT_OK++))
            ((COUNT_STOP++))
        fi
    done <<<"${arquivo}"

    # Condicional limitacao de exibicao (15 itens)
    if [ ${COUNT_OK} -lt "1" ] ;
    then
        # Falha na coleta - Pesquisa vazia
        echo -e "Nenhum Resultado Encontrado Para a Pesquisa: ${ARGUMENT}"
        exit

    elif [ "${#LINHA_CONSULTA[@]}" -gt  "15" ] ;
    then
        read -p "Encontrado ${#LINHA_CONSULTA[@]}, Deseja Exibir Todos ? [Y|N] "  RESPOSTA_EXIB
        if [ "${RESPOSTA_EXIB}" == "y" ] || [ "${RESPOSTA_EXIB}" == "Y" ] ;
        then
            echo -e "\e[00;33m$coluna \e[00m"
            for count_linha in ${LINHA_CONSULTA[@]} ;
            do
                echo -e "${count_linha}"| sed "s/_/ /g" | sed "s/-/ /g"
            done
        else
            echo -e "\e[00;33m$coluna \e[00m"
            for count_linha in ${LINHA_CONSULTA[@]:0:15} ;
            do
                echo -e "${count_linha}"| sed "s/_/ /g"| sed "s/-/ /g"
            done
        fi
    else
        echo -e "\e[00;33m$coluna \e[00m"
        for count_linha in ${LINHA_CONSULTA[@]:0:15} ;
        do
            echo -e "${count_linha}"| sed "s/_/ /g"| sed "s/-/ /g"
        done
    fi

}

login_server () {

    if [ "${FILTRO_IP_ACESSO}" == "234" ] ;
    then
        ## Valor comum ao logar com sucesso no pfsense
        PF_LOGIN_VAR="Welcome to pfSense"
        script -q -c "sshpass -p "2Cm@pf098#" ssh -o UserKnownHostsFile=/dev/null -o GSSAPIAuthentication=no -o  StrictHostKeyChecking=no root@${IP_ACESSO} -p ${PORTA_ACESSO}" ${LOG_ACESSO}
    elif [ "${FILTRO_IP_ACESSO_CLOUD}" == "17" ] ;
    then
        ## Valor comum ao logar com sucesso no pfsense
        PF_LOGIN_VAR="Welcome to pfSense"
        script -q -c "sshpass -p "2Cm@utm098#" ssh -o UserKnownHostsFile=/dev/null -o GSSAPIAuthentication=no -o  StrictHostKeyChecking=no root@${IP_ACESSO} -p ${PORTA_ACESSO}" ${LOG_ACESSO}
    else
        # Acesso inicial
        script -q -c "sshpass -p "ko9@FdN8#Tt*" ssh -o UserKnownHostsFile=/dev/null -o GSSAPIAuthentication=no -o  StrictHostKeyChecking=no 2com@${IP_ACESSO} -p ${PORTA_ACESSO}" ${LOG_ACESSO}
        LOGIN_STATUS=$(cat ${LOG_ACESSO} | grep -i "Last login"| wc -l)
        if [ "${LOGIN_STATUS}" -ge "1" ] ;
        then
            #Acesso Realizado
            echo -e "Acesso Concluido"
        else
            # Possivel falha
            # Teste suse
            script -q -c "sshpass -p "ko9@FdN8#Tt*" ssh -o UserKnownHostsFile=/dev/null -o GSSAPIAuthentication=no -o  StrictHostKeyChecking=no doiscom@${IP_ACESSO} -p ${PORTA_ACESSO}" ${LOG_ACESSO_SUSE}
            LOGIN_STATUS=$(cat ${LOG_ACESSO_SUSE} | grep -i "Last login"| wc -l)
            if [ "${LOGIN_STATUS}" -ge "1" ] ;
            then
                #Acesso Realizado
                echo -e "Acesso Concluido"
            else
                #Acesso Falhou
                echo -e "Acesso Falhou"
            fi
        fi
    fi
}

variaveis_acesso () {
    # Requisitos para Acesso 
    IP_ACESSO=$(echo -e "${IP_CONSULTAS[${1}]}"| awk -F"-" '{print $1}')
    PORTA_ACESSO=$(echo -e "${IP_CONSULTAS[${1}]}"| awk -F"-" '{print $2}')

    # Filtros para Faixas de IP
    FILTRO_IP_ACESSO_CLOUD=$(echo -e "${IP_ACESSO}"|awk -F"." '{print $2}')
    FILTRO_IP_ACESSO=$(echo -e "${IP_ACESSO}"|awk -F"." '{print $3}')
    # Registro de login
    
    GET_USER=$(whoami| awk -F"@" '{print $1}')
    LOG_ACESSO=${DIR_LOG}/acesso_${GET_USER}_${IP_ACESSO}_${DATA}_${HORA}.log
    LOG_ACESSO_SUSE=${DIR_LOG}/acesso_${GET_USER}_${IP_ACESSO}_SUSE_${DATA}_${HORA}.log

    #Confirmacao de acesso
    if [ "$ARGUMENT" == "livre" ] || [ "$ARGUMENT" == "LIVRE" ] ;
    then
        IP_ACESSO_EXIB=$(cat /gitlab/vpn-inventario/hosts | grep -w "${IP_ACESSO}"| awk -F"#" '{print $4}')
    else
        IP_ACESSO_EXIB=$(cat /gitlab/vpn-inventario/hosts | grep -w "${IP_ACESSO}"| awk -F"#" '{print $3}')
    fi 
}

# Funcao de acesso aos servidores listados
interacao_acesso () {
    ## 1 - Primeira Interacao de Acesso 
    read -p "Qual o Numero do Servidor Para Acesso ? "  RESPOSTA_ACESSO
    if [ ${RESPOSTA_ACESSO} == "quit" ] || [ ${RESPOSTA_ACESSO} == "QUIT" ] || [ ${RESPOSTA_ACESSO} == "Q" ] || [ ${RESPOSTA_ACESSO} == "q" ] ;
    then
        echo -e "Encerrado Pelo Usuario"
        exit
    elif [ -n ${RESPOSTA_ACESSO} ] && [[ "${RESPOSTA_ACESSO}" =~ ^[0-9]{1,4}$ ]] && ([ ${RESPOSTA_ACESSO} -gt "0" ] && [ ${RESPOSTA_ACESSO} -lt ${COUNT_OK} ])  ;
    then
                # Funcao de declaração de variaveis
                variaveis_acesso ${RESPOSTA_ACESSO}

                # 1 - Primeira Interacao de confirmação
                read -p "Deseja Acessar este Servidor ? 
${IP_ACESSO} - ${IP_ACESSO_EXIB} - [Y|N]: "  RESPOSTA_CONFIRMACAO

                if [ "${RESPOSTA_CONFIRMACAO}" == "y" ] || [ "${RESPOSTA_CONFIRMACAO}" == "Y" ] ;
                then
                    # função de login
                    login_server
                else
                    echo -e "Acesso Cancelado Pelo Usuario - Realizando Nova Tentativa"
                    # 2- Segunda Interação de acesso
                    read -p "Qual o Numero do Servidor para Acesso ? "  "RESPOSTA_ACESSO"
                    if [ ${RESPOSTA_ACESSO} == "quit" ] || [ ${RESPOSTA_ACESSO} == "QUIT" ] || [ ${RESPOSTA_ACESSO} == "Q" ] || [ ${RESPOSTA_ACESSO} == "q" ] ;
                    then
                        echo -e "Encerrado Pelo Usuario"
                        exit
                    elif  [ -n ${RESPOSTA_ACESSO} ] && [[ "${RESPOSTA_ACESSO}" =~ ^[0-9]{1,4}$ ]] && ([ ${RESPOSTA_ACESSO} -gt "0" ] && [ ${RESPOSTA_ACESSO} -lt ${COUNT_OK} ])  ;
                    then
                        # Funcao de declaração de variaveis
                        variaveis_acesso "${RESPOSTA_ACESSO}"

                ## read sensivel ao espaçamento-  mantido fora da identação propositalmente
                # 2 - Segunda Interacao de confirmação
                read -p "Deseja Acessar este Servidor ?
                ${IP_ACESSO} - ${IP_ACESSO_EXIB} - [Y|N]: "  RESPOSTA_CONFIRMACAO
                        if [ "${RESPOSTA_CONFIRMACAO}" == "y" ] || [ "${RESPOSTA_CONFIRMACAO}" == "Y" ] ;
                        then
                            # função de login
                            login_server
                        else
                            echo -e "Acesso Cancelado Pelo Usuario"
                            exit 
                        fi
                    else
                        #paramentro de acesso nao informado
                        echo -e "Valor de Acesso Nao Informado ou Invalido"
                        exit
                    fi
                fi 
    else
        #paramentro de acesso nao informado
        echo -e "Valor de Acesso Nao Informado ou Invalido"
        echo -e "Acesso Cancelado Pelo Usuario - Realizando Nova Tentativa"
        # 2- Segunda Interação de acesso
        read -p "Qual o Numero do Servidor para Acesso ? "  "RESPOSTA_ACESSO"
        if [ ${RESPOSTA_ACESSO} == "quit" ] || [ ${RESPOSTA_ACESSO} == "QUIT" ] || [ ${RESPOSTA_ACESSO} == "Q" ] || [ ${RESPOSTA_ACESSO} == "q" ] ;
        then
            echo -e "Encerrado Pelo Usuario"
            exit
        elif  [ -n ${RESPOSTA_ACESSO} ] && [[ "${RESPOSTA_ACESSO}" =~ ^[0-9]{1,4}$ ]] && ([ ${RESPOSTA_ACESSO} -gt "0" ] && [ ${RESPOSTA_ACESSO} -lt ${COUNT_OK} ])  ;
        then
            # Funcao de declaração de variaveis
            variaveis_acesso "${RESPOSTA_ACESSO}"

    ## read sensivel ao espaçamento-  mantido fora da identação propositalmente
    # 2 - Segunda Interacao de confirmação
    read -p "Deseja Acessar este Servidor ?
${IP_ACESSO} - ${IP_ACESSO_EXIB} - [Y|N]: "  RESPOSTA_CONFIRMACAO
            if [ "${RESPOSTA_CONFIRMACAO}" == "y" ] || [ "${RESPOSTA_CONFIRMACAO}" == "Y" ] ;
            then
                # função de login
                login_server
            else
                echo -e "Acesso Cancelado Pelo Usuario"
                exit 
            fi
        else
            #paramentro de acesso nao informado
            echo -e "Valor de Acesso Nao Informado ou Invalido"
            exit
        fi
    fi
}

# testa se existe argumento de pesquisa
if [ -z "${1}" ] ;
then
    read -p "CLIENTE : "  ARGUMENT
    if [ -z "${ARGUMENT}" ] ;
    then
        echo "Argumento Nao Declarado"
        exit
    else
        pesquisa_vpn ${ARGUMENT}
        pesquisa_exibicao
        interacao_acesso
    fi
else
    COUNT_ARGUMENT=$(echo -e "${1}"| awk '{ print substr( $0, 0, 2 ) }'| grep "-" | wc -l)
    if [ ${COUNT_ARGUMENT:=0} -gt "0" ] ;
    then
        if [ "${1}" == "-h" ] || [ "${1}" == "--help" ] ;
        then
            echo "################   SYNTAX   ##########################"
            echo " vpn <argumento> <parametro>"
            echo "################ Parametros - Funcao #################"
            echo "                    -h      - Acesso ao manual"
            echo "                    -t      - Exibe todo o Inventario de Hosts VPN"
            exit
        elif [ "${1}" == "-t"  ] ;
        then
            #echo "${arquivo}"
            pesquisa_vpn
        else
            echo "Parametro nao encontrado"
            exit
        fi
    else
        ARGUMENT=$1
        pesquisa_vpn ${ARGUMENT}
        pesquisa_exibicao
        interacao_acesso
    fi
fi


