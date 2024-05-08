from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://localhost:5502/home"
driver.get(url)
time.sleep(2)
                                          #para recorrer el test favor ejecutar  en la terminal python -m pytest  
def insertar_actividad(actividad):
    btn_insertar_nueva = driver.find_element(By.XPATH, '//*[@id="insertarNueva"]')
    btn_insertar_nueva.click()
    time.sleep(2)

    input_documento_field = driver.find_element(By.XPATH, '//*[@id="documento"]')
    input_documento_field.send_keys(actividad['documento'])
    time.sleep(1)

    input_nombre_field = driver.find_element(By.XPATH, '//*[@id="nombre"]')
    input_nombre_field.send_keys(actividad['nombre'])
    time.sleep(1)

    input_tarea_field = driver.find_element(By.XPATH, '//*[@id="tarea"]')
    input_tarea_field.send_keys(actividad['tarea'])
    time.sleep(1)

    input_hora_field = driver.find_element(By.XPATH, '//*[@id="horas"]')
    input_hora_field.send_keys(actividad['horas'])
    time.sleep(1)

    insertar_field = driver.find_element(By.XPATH, '//*[@id="btn_insertar"]')
    insertar_field.click()
    time.sleep(3)

def test_insertar():
    # Paso 1: Navegar al menú de actividades
 
  
    btn_actividad = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "actividad"))
    )
      
    btn_actividad.click()
    time.sleep(2)

    # Luego, puedes llamar a la función insertar_actividad() dentro de test_insertar()
    actividades = [
        {"documento": "123456789", "nombre": "Daniel Ricaurte", "tarea": "Desarrollar Prueba de Selenium", "horas": "8"},
        {"documento": "09876543", "nombre": "Pablo Picasso", "tarea": "Desarrollar Python", "horas": "4"},
        {"documento": "88888888", "nombre": "Boris Diaz", "tarea": "Desarrollo de aplicaciones web", "horas": "12"},
        {"documento": "567891011", "nombre": "Fulano Martinez", "tarea": "java", "horas": "18"},
        {"documento": "32569856", "nombre": "Jesus Medrano", "tarea": "Angular", "horas": "38"}
    ]

    for actividad in actividades:
        insertar_actividad(actividad)

    editar_field =driver.find_element(By.XPATH, '//*[@id="editar"]' )
    editar_field.click()
    time.sleep(1)

    inputDocumento_field =driver.find_element(By.XPATH, '//*[@id="edi_doc"]' )
    inputDocumento_field.send_keys(Keys.CONTROL + "a")
    inputDocumento_field.send_keys(Keys.DELETE)
    inputDocumento_field.send_keys("EDITADO")
    time.sleep(1)

    inputNombre_field =driver.find_element(By.XPATH, '//*[@id="edi_nom"]' )
    inputNombre_field.send_keys(Keys.CONTROL + "a")
    inputNombre_field.send_keys(Keys.DELETE)
    inputNombre_field.send_keys("EDITADO")
    time.sleep(1)

    inputTarea_field =driver.find_element(By.XPATH, '//*[@id="edi_tar"]' )
    inputTarea_field.send_keys(Keys.CONTROL + "a")
    inputTarea_field.send_keys(Keys.DELETE)
    inputTarea_field.send_keys("EDITADO")
    time.sleep(1)

    inputTarea_field =driver.find_element(By.XPATH, '//*[@id="btn_edit"]' )
    inputTarea_field.click()
    time.sleep(3)
    
    driver.quit()
    
test_insertar()


