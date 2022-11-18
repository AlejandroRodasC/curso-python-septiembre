from user import register_user
import pytest
class TestRegisterUSer:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_data = {
                'first_name': 'Alejandro',
                'last_name': 'Rodas',
                'birthdate': '2001-06-05',
                'gender' : 'male',
                'email':'alerodas201444@gmail.com'
            }
    def test_user_is_registered(self):
        #Act
        message = register_user(**self.user_data) #know arguments

        #Assert
        assert message == 'User succesfully registered'

        from user import user_dict
        assert user_dict == self.user_data

    def test_should_raise_an_error_if_gender_is_incorrect(self):
        with  pytest.raises(Exception) as error:
            self.user_data['gender'] = 'incorrect'

            register_user(**self.user_data) #know arguments

        assert str(error.value) == 'Genders can be male, female or others'
    
    def test_should_raise_an_error_if_email_is_incorrect(self):
        with  pytest.raises(Exception) as error:
            self.user_data.update({'email': 'formato_incorrecto-de-email'})

            register_user(**self.user_data) #know arguments

        assert str(error.value) == 'Incorrect email format'