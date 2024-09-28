import { Banknote, Home } from "lucide-react"
import { Link } from "react-router-dom"

const AppSidebar = () => {
  const listMenus = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: <Home />,
    },
    {
      name: "Transactions",
      path: "/transactions",
      icon: <Banknote />
    }
  ]
  return (
    <div className="bg-primary text-white rounded-md min-h-screen w-64 px-6 py-8 flex flex-col gap-6">
      {
        listMenus.map((item, index) => (
          <Link to={item.path} key={index} className="flex items-center text-white gap-4">
            {item.icon}
            {item.name}
          </Link>
        ))
      }
    </div>
  )
}

export default AppSidebar