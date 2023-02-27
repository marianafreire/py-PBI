import os
from libs.class_dataframe import Dataframe
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    csv_folder_path = os.getenv('PATH_CSV')

    # create folder path and check if it's a string
    if not isinstance(csv_folder_path, str):
        raise TypeError("O caminho da pasta CSV precisa ser uma string")

    # create object
    old_df_path = os.path.join(csv_folder_path, 'State_of_Data_2021_str.csv')
    df = Dataframe(old_df_path)

    # select specific columns to reduce dataframe and make it easier to work with
    preserved_columns = ["('P0', 'id')","('P1_a ', 'Idade')","('P1_b ', 'Genero')", "('P1_e_b ', 'Regiao onde mora')", "('P1_h ', 'Nivel de Ensino')", "('P2_f ', 'Cargo Atual')", "('P2_g ', 'Nivel')","('P2_h ', 'Faixa salarial')","('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')","('P2_q ', 'Atualmente qual a sua forma de trabalho?')","('P2_r ', 'Qual a forma de trabalho ideal para você?')","('P2_a ', 'Qual sua situação atual de trabalho?')","('P2_o ', 'Quais os principais critérios que você leva em consideração no momento de decidir onde trabalhar?')","('P2_o_a ', 'Remuneração/Salário')","('P2_o_b ', 'Benefícios')","('P2_o_c ', 'Propósito do trabalho e da empresa')","('P2_o_d ', 'Flexibilidade de trabalho remoto')","('P2_o_e ', 'Ambiente e clima de trabalho')","('P2_o_f ', 'Oportunidade de aprendizado e trabalhar com referências na área')","('P2_o_g ', 'Plano de carreira e oportunidades de crescimento profissional')","('P2_o_h ', 'Maturidade da empresa em termos de tecnologia e dados')"]
    df.reduce_columns(preserved_columns)

    # change types of columns to make Power BI recognize it
    numeric_columns = ["('P1_a ', 'Idade')","('P2_o_a ', 'Remuneração/Salário')","('P2_o_b ', 'Benefícios')","('P2_o_c ', 'Propósito do trabalho e da empresa')","('P2_o_d ', 'Flexibilidade de trabalho remoto')","('P2_o_e ', 'Ambiente e clima de trabalho')","('P2_o_f ', 'Oportunidade de aprendizado e trabalhar com referências na área')","('P2_o_g ', 'Plano de carreira e oportunidades de crescimento profissional')","('P2_o_h ', 'Maturidade da empresa em termos de tecnologia e dados')"]
    df.change_columns_type(numeric_columns)

    # save 'new_df.csv' on specific path
    df.create_csv(csv_folder_path,'short_dataset.csv')
