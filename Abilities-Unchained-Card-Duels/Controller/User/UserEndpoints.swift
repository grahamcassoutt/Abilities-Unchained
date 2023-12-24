import Foundation

class UserEndpoints {
    let BASE_URL = "http://127.0.0.1:5000/api/"
    
    var GET_USER: String {
        return BASE_URL + "user/"
    }

    func GetUser() async throws -> User? {
        print("here")
        if let url = URL(string: GET_USER) {
            var request = URLRequest(url: url)
            request.httpMethod = "GET"
            
//            do {
//                print("Get User")
//
//
//            } catch {
//                throw error
//            }
        }
        
        return nil
    }
}
