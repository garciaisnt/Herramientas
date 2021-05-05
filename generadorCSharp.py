# 04- mayo -2021
# Carlos Garcia - @garciaisnt

tablaNombre = input("-> Escribe el nombre de la tabla: ")
nCampos = int(input("-> Escribe el NUMERO de campos de la tabla: "))

i = 0
nomCampos = []
while i < nCampos:  
  nomCampos.append(input("-> Escribe el nombre del campo #"+str(i+1)+": "))  
  i= i+1

##------------------------------------------------------
def camposConThis(campos): 
  retorno  = ""
  if(len(campos) == 1):
      retorno = f"\'\" + this._{campos[0]} + \"\'"
  else:
    for i in range(len(campos)):      
      retorno += f"\'\" + this._{campos[i]} + \"\', "
    
    retorno = retorno[0:(len(retorno) - 2)]      
  return retorno

def generarGuardar(campos):
  camposUnidos = ', '.join(campos)
  template = """
  public Boolean Guardar()
  {
      Boolean Resultado = false;
      String Sentencia = @"INSERT INTO %s(%s) VALUES(%s);";
      try
      {
          DataManager.CLS.OperacionBD Operacion = new DataManager.CLS.OperacionBD();
          if (Operacion.Insertar(Sentencia) > 0)
          {
              Resultado = true;
          }
          else
          {
              Resultado = false;
          }
      }
      catch
      {
          Resultado = false;
      }

      return Resultado;
  }""" % (tablaNombre, camposUnidos, camposConThis(campos))

  return template


def generarEditar(campos):

    camposEditar = ""

    if(len(campos) == 1):
      camposEditar = f"SET {campos[0]} = \'\" + this._{campos[0]} + \"\'"
    else:
        for i in range(len(campos)):      
            camposEditar += f"SET {campos[i]} = \'\" + this._{campos[i]} + \"\', "

    camposEditar = camposEditar[0:(len(camposEditar) - 2)]

    template = """
    public Boolean Editar()
    {
        Boolean Resultado = false;
        String Sentencia = @"UPDATE %s %s WHERE %s = " + this._%s + ";";

        try
        {
            DataManager.CLS.OperacionBD Operacion = new DataManager.CLS.OperacionBD();
            if (Operacion.Actualizar(Sentencia) > 0)
            {
                Resultado = true;
            }
            else
            {
                Resultado = false;
            }
        }
        catch
        {
            Resultado = false;
        }

        return Resultado;
    }""" % (tablaNombre, camposEditar, campos[0], campos[0])

    return template

def generarEliminar(campos):  
    template = """
    public Boolean Eliminar()
    {
        Boolean Resultado = false;
        String Sentencia = @"DELETE FROM %s WHERE %s = " + this._%s + ";";

        try
        {
            DataManager.CLS.OperacionBD Operacion = new DataManager.CLS.OperacionBD();
            if (Operacion.Eliminar(Sentencia) > 0)
            {
                Resultado = true;
            }
            else
            {
                Resultado = false;
            }
        }
        catch
        {
            Resultado = false;
        }

        return Resultado;
    }""" % (tablaNombre, campos[0], campos[0])

    return template


##Genracion de 
print("----------GUARDAR----------")
print(generarGuardar(nomCampos))
print("----------MODIFICAR----------")
print(generarEditar(nomCampos))
print("----------ELIMININAR----------")
print(generarEliminar(nomCampos))





  
    
