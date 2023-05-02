#Interfaz
class InformalParserInterface:
  def load_data_source(self, path: str, file_name: str) -> str:
    """Load in the file for extracting text."""
    pass

  def extract_text(self, full_file_name: str) -> dict:
    """Extract text from the currently loaded file."""
    pass

#Clases concreta 1
class PdfParser(InformalParserInterface):
  """Extract text from a PDF"""
  def load_data_source(self, path: str, file_name: str) -> str:
    """Overrides InformalParserInterface.load_data_source()"""
    pass

  def extract_text(self, full_file_path: str) -> dict:
    """Overrides InformalParserInterface.extract_text()"""
    pass

#Clases concreta 2
#En esta clase no se implementa por completo la estructura de la interfaz --> bajo reglas estrictas, se genera error
class EmlParser(InformalParserInterface):
  """Extract text from an email"""
  def load_data_source(self, path: str, file_name: str) -> str:
      """Overrides InformalParserInterface.load_data_source()"""
      pass

  def extract_text_from_email(self, full_file_path: str) -> dict:
      """A method defined only in EmlParser.
      Does not override InformalParserInterface.extract_text()
      """
      pass


#Si no se implementa una interfaz por completo, no debería existir relación de herencia
print(issubclass(PdfParser, InformalParserInterface))
print(issubclass(EmlParser, InformalParserInterface)) #Esta debería ser False