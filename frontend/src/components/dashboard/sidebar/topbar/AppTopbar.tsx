import { UserRound } from 'lucide-react'

const AppTopbar = () => {
  return (
    <div className='flex justify-end mr-6 mt-3 gap-2 cursor-pointer'>
      <h6 className='font-semibold'>Vivek Kumar</h6> <UserRound className='h-6 w-6' />
    </div>
  )
}

export default AppTopbar